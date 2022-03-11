import enum
import math
from typing import Callable, Dict, List, Tuple
from numpy.random import default_rng as defaultRng
import numpy as np

def rs():
    """
    Returns a random seed.
    """
    return np.random.randint(0,9999999)

Gender = enum.Enum("Φύλο", "Αρσενικό Θηλυκό Ουδέτερο")
Case = enum.Enum("Πτώση", "Ονομαστική Γενική Δοτική Αιτιατική Κλητική")
Person = enum.Enum("Πρόσωπο", "Α Β Γ")
Number = enum.Enum("Αριθμός", "Ενικός Δυϊκός Πληθυντικός")
Tense = enum.Enum("Χρόνος", "Ενεστώτας Αόριστος Παρατατικός Παρακείμενος Υπερσυντέλικος ΜέλλονταςΣυντελεσμένος ΜέλλονταςΕξακολουθητηκός")
Mood = enum.Enum("Έγκλιση", "Οριστική Υποτακτική Προστακτική Ευκτική")
Voice = enum.Enum("Φωνή", "Ενεργητική Μέση Παθητική")
Definite = bool

defaultGender = Gender.Αρσενικό
defaultCase = Case.Ονομαστική
defaultPerson = Person.Α
defaultNumber = Number.Ενικός
defaultTense = Tense.Ενεστώτας
defaultMood = Mood.Οριστική

class Word:

    def __init__(self,
                 words: List[str],
                 probabilities: List[float]):
        assert len(words) == len(probabilities), f"Expected two lists of the same length, got: {words} and {probabilities} instead."
        assert math.isclose(np.sum(probabilities), 1.0, abs_tol=1e-9), f"Expected probabilities that sum to one. Got {probabilities} instead"
        self.words = words
        self.probabilities = probabilities
        seed = rs()
        self.rng = defaultRng(seed)
    
    def get_word(self, filter_vesions) -> str:
        choices = filter_vesions(self.words, self.probabilities)
        s = self.rng.choice(self.words, p=self.probabilities)
        while not s in choices:
            s = self.rng.choice(self.words, p=self.probabilities)
        return s


VerbConjugationDict = Dict[Tuple[Mood, Number, Person, Tense, Voice], Word]
NounDeclensionDict = Dict[Tuple[Case, Gender, Number], Word]
ArticleDeclensionDict = Dict[Tuple[Case, Definite, Gender, Number], Word]
AdjectiveDeclensionDict = NounDeclensionDict

defaultVerbForm = (defaultMood, defaultNumber, defaultPerson, defaultTense)
defaultNounForms = {
    'masculine': (defaultCase, Gender.Αρσενικό, defaultNumber),
    'feminine': (defaultCase, Gender.Θηλυκό, defaultNumber),
    'neuter': (defaultCase, Gender.Ουδέτερο, defaultNumber),
}
defaultArticleForms = {
    ('definite', 'masculine'): (defaultCase, True, Gender.Αρσενικό, defaultNumber),
    ('definite', 'feminine'): (defaultCase, True, Gender.Θηλυκό, defaultNumber),
    ('definite', 'neuter'): (defaultCase, True, Gender.Ουδέτερο, defaultNumber),
    ('indefinite', 'masculine'): (defaultCase, False, Gender.Αρσενικό, defaultNumber),
    ('indefinite', 'feminine'): (defaultCase, False, Gender.Θηλυκό, defaultNumber),
    ('indefinite', 'neuter'): (defaultCase, False, Gender.Ουδέτερο, defaultNumber),
}
defaultAdjectiveForms = defaultNounForms

def default_versions_filter(words: List[str], probabilities: List[float]) -> List[str]:
    return words

class PartOfSpeech:
    
    def get_default_form(self) -> str:
        return self.default_form

class Noun(PartOfSpeech):

    def __init__(self,
                 declension_dict: NounDeclensionDict,
                 kyrio: bool = False):
        self.declension_dict: NounDeclensionDict = declension_dict
        self.kyrio = kyrio

        cases = list(Case)
        genders = list(Gender)
        numbers = list(Number)

        for case in cases:
            for gender in genders:
                for number in numbers:
                    s = self.get_form(case, gender, number)
                    if not s is None:
                        self.default_form = s
                        return
    
    def get_form(self, πτώση: Case, φύλο: Gender, αριθμός: Number, filter_versions: Callable = default_versions_filter) -> str:
        w = self.declension_dict.get((πτώση, φύλο, αριθμός))
        if w is None:
            return None
        return w.get_word(filter_versions)
    
    

class Verb(PartOfSpeech):

    def __init__(self,
                 conjugation_dict: VerbConjugationDict,
                 katigoroumeno: bool = False):
        self.conjugation_dict: VerbConjugationDict = conjugation_dict
        self.katigoroumeno = katigoroumeno

    
    def get_form(self, έγκλιση: Mood, αριθμός: Number, πρόσωπο: Person, χρόνος:Tense, φωνή:Voice, filter_versions: Callable = default_versions_filter) -> str:
        w = self.conjugation_dict.get((έγκλιση, αριθμός, πρόσωπο, χρόνος, φωνή))
        if w is None:
            return None
        return w.get_word(filter_versions)

class Article(PartOfSpeech):

    def __init__(self):
        self.declension_dict: ArticleDeclensionDict = {
            (Case.Ονομαστική, False, Gender.Αρσενικό, Number.Ενικός): Word(["ὁ"], [1]),
            (Case.Ονομαστική, False, Gender.Αρσενικό, Number.Πληθυντικός): Word(["οἱ"], [1]),
            (Case.Γενική, False, Gender.Αρσενικό, Number.Ενικός): Word(["τοῦ"], [1]),
            (Case.Γενική, False, Gender.Αρσενικό, Number.Πληθυντικός): Word(["τῶν"], [1]),
            (Case.Δοτική, False, Gender.Αρσενικό, Number.Ενικός):  Word(["τῷ"], [1]),
            (Case.Δοτική, False, Gender.Αρσενικό, Number.Πληθυντικός):  Word(["τοῖς"], [1]),
            (Case.Αιτιατική, False, Gender.Αρσενικό, Number.Ενικός):  Word(["τόν"], [1]),
            (Case.Αιτιατική, False, Gender.Αρσενικό, Number.Πληθυντικός):  Word(["τούς"], [1]),
            (Case.Κλητική, False, Gender.Αρσενικό, Number.Ενικός):  Word(["ὦ", ""], [0.2, 0.8]),
            (Case.Κλητική, False, Gender.Αρσενικό, Number.Πληθυντικός):  Word(["ὦ", ""], [0.2, 0.8]),
            (Case.Ονομαστική, False, Gender.Θηλυκό, Number.Ενικός): Word(["ἡ"], [1]),
            (Case.Ονομαστική, False, Gender.Θηλυκό, Number.Πληθυντικός): Word(["οἱ", "αἱ"], [0.8, 0.2]),
            (Case.Γενική, False, Gender.Θηλυκό, Number.Ενικός): Word(["τῆς"], [1]),
            (Case.Γενική, False, Gender.Θηλυκό, Number.Πληθυντικός): Word(["τῶν"], [1]),
            (Case.Δοτική, False, Gender.Θηλυκό, Number.Ενικός):  Word(["τῇ"], [1]),
            (Case.Δοτική, False, Gender.Θηλυκό, Number.Πληθυντικός):  Word(["ταῖς"], [1]),
            (Case.Αιτιατική, False, Gender.Θηλυκό, Number.Ενικός):  Word(["τήν"], [1]),
            (Case.Αιτιατική, False, Gender.Θηλυκό, Number.Πληθυντικός):  Word(["τις", "τάς"], [0.8, 0.2]),
            (Case.Κλητική, False, Gender.Θηλυκό, Number.Ενικός):  Word(["ὦ", ""], [0.2, 0.8]),
            (Case.Κλητική, False, Gender.Θηλυκό, Number.Πληθυντικός):  Word(["ὦ", ""], [0.2, 0.8]),
            (Case.Ονομαστική, False, Gender.Ουδέτερο, Number.Ενικός): Word(["τό"], [1]),
            (Case.Ονομαστική, False, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["τά"], [1]),
            (Case.Γενική, False, Gender.Ουδέτερο, Number.Ενικός): Word(["τοῦ"], [1]),
            (Case.Γενική, False, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["τῶν"], [1]),
            (Case.Δοτική, False, Gender.Ουδέτερο, Number.Ενικός):  Word(["τῷ"], [1]),
            (Case.Δοτική, False, Gender.Ουδέτερο, Number.Πληθυντικός):  Word(["τοῖς"], [1]),
            (Case.Αιτιατική, False, Gender.Ουδέτερο, Number.Ενικός):  Word(["τό"], [1]),
            (Case.Αιτιατική, False, Gender.Ουδέτερο, Number.Πληθυντικός):  Word(["τά"], [1]),
            (Case.Κλητική, False, Gender.Ουδέτερο, Number.Ενικός):  Word(["ὦ", ""], [0.2, 0.8]),
            (Case.Κλητική, False, Gender.Ουδέτερο, Number.Πληθυντικός):  Word(["ὦ", ""], [0.2, 0.8]),

            
            (Case.Ονομαστική, True, Gender.Αρσενικό, Number.Ενικός): Word(["ἕνας", "εἷς"], [0.8, 0.2]),
            (Case.Γενική, True, Gender.Αρσενικό, Number.Ενικός): Word(["ἑνός"], [1]),
            (Case.Δοτική, True, Gender.Αρσενικό, Number.Ενικός):  Word(["ἑνί"], [1]),
            (Case.Αιτιατική, True, Gender.Αρσενικό, Number.Ενικός):  Word(["ἕναν"], [1]),
            (Case.Ονομαστική, True, Gender.Θηλυκό, Number.Ενικός): Word(["μία", "μια"], [0.5, 0.5]),
            (Case.Γενική, True, Gender.Θηλυκό, Number.Ενικός): Word(["μίας", "μιᾶς"], [0.5, 0.5]),
            (Case.Δοτική, True, Gender.Θηλυκό, Number.Ενικός):  Word(["μιᾷ"], [1]),
            (Case.Αιτιατική, True, Gender.Θηλυκό, Number.Ενικός):  Word(["μίαν", "μιάν"], [0.7, 0.3]),
            (Case.Ονομαστική, True, Gender.Ουδέτερο, Number.Ενικός): Word(["ἕνα", "ἕν"], [0.7, 0.3]),
            (Case.Γενική, True, Gender.Ουδέτερο, Number.Ενικός): Word(["ἑνός"], [1]),
            (Case.Δοτική, True, Gender.Ουδέτερο, Number.Ενικός):  Word(["ἑνί"], [1]),
            (Case.Αιτιατική, True, Gender.Ουδέτερο, Number.Ενικός):  Word(["ἕνα", "ἕν"], [0.7, 0.3]),
        }
        self.default_form = self.get_form(Case.Ονομαστική, False, Gender.Αρσενικό, Number.Ενικός)

    def get_form(self, πτώση: Case, αόριστο: bool, φύλο: Gender, αριθμός: Number, filter_versions: Callable = default_versions_filter) -> str:
        w = self.declension_dict.get((πτώση, αόριστο, φύλο, αριθμός))
        if w is None:
            return None
        return w.get_word(filter_versions)

class Adjective(PartOfSpeech):

    def __init__(self,
                 declension_dict: AdjectiveDeclensionDict):
        self.declension_dict: AdjectiveDeclensionDict = declension_dict

        cases = list(Case)
        genders = list(Gender)
        numbers = list(Number)

        for case in cases:
            for gender in genders:
                for number in numbers:
                    s = self.get_form(case, gender, number)
                    if not s is None:
                        self.default_form = s
                        return
    
    def get_form(self, πτώση: Case, φύλο: Gender, αριθμός: Number, filter_versions: Callable = default_versions_filter) -> str:
        w = self.declension_dict.get((πτώση, φύλο, αριθμός))
        if w is None:
            return None
        return w.get_word(filter_versions)

class Adverb(PartOfSpeech):

    def __init__(self,
                 it: str):
        self.it = it
        self.default_form = it

