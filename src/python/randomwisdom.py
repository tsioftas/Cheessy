from ctypes import Union
from enum import Enum
from typing import List, Dict, Tuple
import numpy as np
from numpy.random import default_rng as defaultRng
from grammar import PartOfSpeech, Noun, Adjective, Verb, Adverb, Article, Word, \
                    Case, Definite, Gender, Mood, Number, Person, Tense, Voice, \
                    NounDeclensionDict, AdjectiveDeclensionDict, VerbConjugationDict, \
                    defaultCase, defaultGender, defaultMood, defaultNumber, defaultPerson, defaultTense
from vocabulary import grammar_to_str

class Vocabulary:

    def __init__(self,
                 nouns,
                 adjectives,
                 verbs,
                 adverbs
                 ):
        self.nouns: List[Noun] = nouns
        self.adjectives: List[Adjective] = adjectives
        self.verbs: List[Verb] = verbs
        self.adverbs: List[Adverb] = adverbs
        self.article: Article = Article()

class Importer:

    str_to_grammar = {v: k for k, v in grammar_to_str.items()}

    def tuple_to_word(t: Tuple[List[str], List[float]]) -> Word:
        return Word(t[0], t[1])

    def str_to_part_of_speech(s: str) -> type:
        d = {
            "noun": Noun,
            "verb": Verb,
            "adjective": Adjective
        }
        return d[s]

    def string_to_tuple(s: str) -> Tuple:
        tokens = s.split("#")
        pOs = Importer.str_to_part_of_speech(tokens.pop(0))
        if pOs == "noun":
            kyrio = tokens.pop(0) == "True"
        else:
            kyrio = None
        grammar_tokens = [Importer.str_to_grammar[token] for token in tokens]
        return [pOs, kyrio], tuple(grammar_tokens)

    def loaded_data_to_lists_of_objects(data: List[Dict[str,Tuple[List[str], List[float]]]]) -> List[PartOfSpeech]:
        
        objects: List[PartOfSpeech] = []
        for conjdecldict in data:
            d = {}
            for word, p in conjdecldict.items():
                pOs, tuple = Importer.string_to_tuple(word)
                word = Importer.tuple_to_word(p)
                d[tuple] = word
            if pOs[0] == Noun:
                obj = Noun(d, pOs[1])
            else:
                obj = pOs[0](d)
            objects.append(obj)

        return objects

    def import_vocabulary(verbose=True) -> Vocabulary:
        if verbose:
            print("Loading vocabulary...")

        article = Article()

        nouns_filename = "data/glossarion/ousiastika.npy"
        adjectives_filename = "data/glossarion/epitheta.npy"
        verbs_filename = "data/glossarion/rimata.npy"
        adverbs_filename = "data/glossarion/epirrimata.npy"

        with open(nouns_filename, "rb") as f:
            nouns_nparray = np.load(f, allow_pickle=True)
        with open(adjectives_filename, "rb") as f:
            adjectives_nparray = np.load(f, allow_pickle=True)
        with open(verbs_filename, "rb") as f:
            verbs_nparray = np.load(f, allow_pickle=True)
        with open(adverbs_filename, "rb") as f:
            adverbs_nparray = np.load(f, allow_pickle=True)
        
        nouns_list: List[Noun] = Importer.loaded_data_to_lists_of_objects(nouns_nparray)
        adjectives_list: List[Adjective] = Importer.loaded_data_to_lists_of_objects(adjectives_nparray)
        verbs_list: List[Verb] = Importer.loaded_data_to_lists_of_objects(verbs_nparray)
        adverbs_list: List[Adverb] = [Adverb(adv) for adv in adverbs_nparray]

        if verbose:
            print("Adding nouns...")
        nouns = []
        for noun in nouns_list:
            nouns.append(noun)
            g = None
            for gender in list(Gender):
                noun_str = noun.get_form(defaultCase, gender, defaultNumber)
                if not noun_str is None:
                    g = gender
                    break
            article_str = article.get_form(defaultCase, False, g, defaultNumber)
            if verbose:
                print(f"- {article_str} {noun_str}")
        
        if verbose:
            print("Adding adjectives...")
        adjectives = []
        for adjective in adjectives_list:
            adjectives.append(adjective)
            adjectiveForm = None
            g = None
            for gender in list(Gender):
                adjective_str = adjective.get_form(defaultCase, gender, defaultNumber)
                if not adjective_str is None:
                    g = gender
                    break
            article_str = article.get_form(defaultCase, False, gender, defaultNumber)
            if verbose:
                print(f"- {article_str} {adjective_str}")
        
        if verbose:
            print("Adding verbs...")
        verbs = []
        for verb in verbs_list:
            verbs.append(verb)
            for voice in list(Voice):
                verb_str = verb.get_form(defaultMood, defaultNumber, defaultPerson, defaultTense, voice)
                if not verb_str is None:
                    break
            if verbose:
                print(f"- {verb_str}")
        
        if verbose:
            print("Adding adverbs...")
        adverbs = []
        for adverb in adverbs_list:
            adverbs.append(adverb)
            adverb_str = adverb.it
            if verbose:
                print(f"- {adverb_str}")
        
        return nouns, adjectives, verbs, adverbs

class WiseOne:

    def __init__(self):
        nouns, adjectives, verbs, adverbs = Importer.import_vocabulary()
        self.vocabulary = Vocabulary(nouns, adjectives, verbs, adverbs)
        self.rng = defaultRng(np.random.randint(0, 9999999))

        # Grammar rules
        self.subjects: List[List[PartOfSpeech]] = [
            self.vocabulary.adjectives,
            self.vocabulary.nouns
        ]

        self.objects: List[List[PartOfSpeech]] = [
            self.vocabulary.adjectives,
            self.vocabulary.nouns
        ]

        self.katigoroumena: List[List[PartOfSpeech]] = [
            self.vocabulary.adjectives,
            self.vocabulary.nouns
        ]
    
    def getSaying(self):
        return self.get_random_sentence()
    
    def get_random_subject(self) -> PartOfSpeech:
        return self.rng.choice([self.rng.choice(t) for t in self.subjects])

    def get_random_verb(self) -> Verb:
        return self.rng.choice(self.vocabulary.verbs)
    
    def get_random_katigoroumeno(self) -> PartOfSpeech:
        return self.rng.choice([self.rng.choice(t) for t in self.katigoroumena])
        
    def get_random_object(self) -> PartOfSpeech:
        return self.rng.choice([self.rng.choice(t) for t in self.objects])

    def get_random_sentence(self) -> str:
               
        # Choose subject
        subject: Union[Noun,Adjective] = self.get_random_subject()
        p_article_subject = 0.7
        if type(subject) == Noun and subject.kyrio:
            p_article_subject = 1
        genders: List[Gender] = self.get_random_order(Gender)
        numbers: List[Number] = self.get_random_order(Number)
        s_case = Case.Ονομαστική
        subject_str = None
        found = False
        for s_number in numbers:
            for s_gender in genders:
                subject_str = subject.get_form(s_case, s_gender, s_number)
                if not subject_str is None:
                    found = True
                    break
            if found:
                break
        if subject_str is None:
            print(f"Did not find {subject.get_default_form()}")
            subject_str = ""
        if self.rng.random() <= p_article_subject:
            subject_article_str = ""
        else:
            s_a_definite = self.rng.choice([True, False])
            article = self.vocabulary.article.get_form(s_case, s_a_definite, s_gender, s_number)
            if article is None:
                subject_article_str = ""
            else:
                subject_article_str = article + " "
            if subject_article_str is None:
                subject_article_str = ""
        subject_str = subject_article_str + subject_str

        # Choose verb
        verb = self.get_random_verb()
        moods = self.get_random_order(Mood)
        v_number = s_number
        persons = [Person.Γ] # self.get_random_order(Person)
        tenses = self.get_random_order(Tense)
        voices = self.get_random_order(Voice)
        verb_str = None
        found = False
        for v_mood in moods:
            for v_person in persons:
                for v_tense in tenses:
                    for v_voice in voices:
                        verb_str = verb.get_form(v_mood, v_number, v_person, v_tense, v_voice)
                        if not verb_str is None:
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
            if found:
                break
        
        # Omit subject?
        p_omit_subject = 0.1 if v_person == Person.Γ else 0
        if self.rng.random() <= p_omit_subject:
            subject_str = ""

        # Choose other
        p_article_other = 0.5
        other: Union[Noun,Adjective] = None
        if verb.katigoroumeno:
            other = self.get_random_katigoroumeno()
            o_case = Case.Ονομαστική
        else:
            other = self.get_random_object()
            o_case = Case.Αιτιατική
        if type(other) == Noun and other.kyrio:
            p_article_other = 1
        genders: Gender = self.get_random_order(Gender)
        numbers: Number = self.get_random_order(Number)
        other_str = None
        found = False
        for o_gender in genders:
            for o_number in numbers:
                other_str = other.get_form(o_case, o_gender, o_number)
                if not other_str is None:
                    found = True
                    break
            if found:
                break
        other_article_str = None
        if self.rng.random() <= p_article_subject:
            other_article_str = ""
        else:
            o_a_definite = self.rng.choice([True, False])
            article = self.vocabulary.article.get_form(o_case, o_a_definite, o_gender, o_number)
            if article is None:
                other_article_str = ""
            else:
                other_article_str = article + " "
            if other_article_str is None:
                other_article_str = ""
        other_str = other_article_str + other_str

        sentence_elements = [other_str, subject_str, verb_str]
        self.rng.shuffle(sentence_elements)
        return sentence_elements[0] + " " + sentence_elements[1] + " " + sentence_elements[2]
        
    def get_random_order(self, e: Enum):
        l = list(e)
        self.rng.shuffle(l)
        return l