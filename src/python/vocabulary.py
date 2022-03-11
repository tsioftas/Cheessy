from typing import Any, Dict, List, Tuple
import numpy as np
from grammar import PartOfSpeech, Noun, Adjective, Verb, Adverb, Article, Word, \
                    Case, Definite, Gender, Mood, Number, Person, Tense, Voice, \
                    NounDeclensionDict, AdjectiveDeclensionDict, VerbConjugationDict

# Nouns

# Nouns/Masculine

Visos = Noun({
    (Case.Ονομαστική, Gender.Αρσενικό, Number.Ενικός): Word(["Βίσος"], [1]),
    (Case.Γενική, Gender.Αρσενικό, Number.Ενικός): Word(["Βίσου"], [1]),
    (Case.Δοτική, Gender.Αρσενικό, Number.Ενικός): Word(["Βίσῳ"], [1]),
    (Case.Αιτιατική, Gender.Αρσενικό, Number.Ενικός): Word(["Βίσον"], [1]),
    (Case.Κλητική, Gender.Αρσενικό, Number.Ενικός): Word(["Βίσε"], [1]),
}, kyrio=True)

Evripidis = Noun({
    (Case.Ονομαστική, Gender.Αρσενικό, Number.Ενικός): Word(["Εὐριπίδης"], [1]),
    (Case.Γενική, Gender.Αρσενικό, Number.Ενικός): Word(["Εὐριπίδη", "Εὐριπίδου"], [0.8, 0.2]),
    (Case.Δοτική, Gender.Αρσενικό, Number.Ενικός): Word(["Εὐριπίδῃ"], [1]),
    (Case.Αιτιατική, Gender.Αρσενικό, Number.Ενικός): Word(["Εὐριπίδην"], [1]),
    (Case.Κλητική, Gender.Αρσενικό, Number.Ενικός): Word(["Εὐριπίδη"], [1]),
}, kyrio=True)

Matthaios = Noun({
    (Case.Ονομαστική, Gender.Αρσενικό, Number.Ενικός): Word(["Ματθαῖος"], [1]),
    (Case.Γενική, Gender.Αρσενικό, Number.Ενικός): Word(["Ματθαίου"], [1]),
    (Case.Δοτική, Gender.Αρσενικό, Number.Ενικός): Word(["Ματθαίῳ"], [1]),
    (Case.Αιτιατική, Gender.Αρσενικό, Number.Ενικός): Word(["Ματθαῖον"], [1]),
    (Case.Κλητική, Gender.Αρσενικό, Number.Ενικός): Word(["Ματθαῖε", "Ματθαῖο"], [0.8, 0.2]),
}, kyrio=True)

Andrianos = Noun({
    (Case.Ονομαστική, Gender.Αρσενικό, Number.Ενικός): Word(["Ἀνδριανός"], [1]),
    (Case.Γενική, Gender.Αρσενικό, Number.Ενικός): Word(["Ἀνδριανοῦ"], [1]),
    (Case.Δοτική, Gender.Αρσενικό, Number.Ενικός): Word(["Ἀνδριανῷ"], [1]),
    (Case.Αιτιατική, Gender.Αρσενικό, Number.Ενικός): Word(["Ἀνδριανόν"], [1]),
    (Case.Κλητική, Gender.Αρσενικό, Number.Ενικός): Word(["Ἀνδριανέ"], [1]),
}, kyrio=True)

Hitler = Noun({
    (Case.Ονομαστική, Gender.Αρσενικό, Number.Ενικός): Word(["Χίτλερ", "Αδόλφος Χίτλερ"], [0.8, 0.2]),
    (Case.Γενική, Gender.Αρσενικό, Number.Ενικός): Word(["Χίτλερ", "Αδόλφου Χίτλερ"], [0.8, 0.2]),
    (Case.Δοτική, Gender.Αρσενικό, Number.Ενικός): Word(["Χίτλερ", "Αδόλφῳ Χίτλερ"], [0.8, 0.2]),
    (Case.Αιτιατική, Gender.Αρσενικό, Number.Ενικός): Word(["Χίτλερ", "Αδόλφον Χίτλερ"], [0.8, 0.2]),
    (Case.Κλητική, Gender.Αρσενικό, Number.Ενικός): Word(["Χίτλερ", "Αδόλφε Χίτλερ"], [0.8, 0.2]),
}, kyrio=True)

karaolos = Noun({
    (Case.Ονομαστική, Gender.Αρσενικό, Number.Ενικός): Word(["καράολος"], [1]),
    (Case.Γενική, Gender.Αρσενικό, Number.Ενικός): Word(["καραόλου"], [1]),
    (Case.Δοτική, Gender.Αρσενικό, Number.Ενικός): Word(["καραόλῳ"], [1]),
    (Case.Αιτιατική, Gender.Αρσενικό, Number.Ενικός): Word(["καράολον"], [1]),
    (Case.Κλητική, Gender.Αρσενικό, Number.Ενικός): Word(["καράολε"], [1]),
    (Case.Ονομαστική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["καράολοι", "καραόλοι"], [0.8, 0.2]),
    (Case.Γενική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["καραόλων"], [1]),
    (Case.Δοτική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["καραόλοις"], [1]),
    (Case.Αιτιατική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["καράολους", "καραόλους"], [0.8, 0.2]),
    (Case.Κλητική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["καράολοι", "καραόλοι"], [0.8, 0.2]),
})

# Nouns/Feminine

Valentina = Noun({
    (Case.Ονομαστική, Gender.Θηλυκό, Number.Ενικός): Word(["Βαλεντίνα"], [1]),
    (Case.Γενική, Gender.Θηλυκό, Number.Ενικός): Word(["Βαλεντίνας"], [1]),
    (Case.Δοτική, Gender.Θηλυκό, Number.Ενικός): Word(["Βαλεντίνᾳ"], [1]),
    (Case.Αιτιατική, Gender.Θηλυκό, Number.Ενικός): Word(["Βαλεντίναν"], [1]),
    (Case.Κλητική, Gender.Θηλυκό, Number.Ενικός): Word(["Βαλεντίνα"], [1]),
}, kyrio=True)

mpyra = Noun({
    (Case.Ονομαστική, Gender.Θηλυκό, Number.Ενικός): Word(["μπύρα"], [1]),
    (Case.Γενική, Gender.Θηλυκό, Number.Ενικός): Word(["μπύρας"], [1]),
    (Case.Δοτική, Gender.Θηλυκό, Number.Ενικός): Word(["μπύρᾳ"], [1]),
    (Case.Αιτιατική, Gender.Θηλυκό, Number.Ενικός): Word(["μπύραν", "μπύρα"], [0.2, 0.8]),
    (Case.Κλητική, Gender.Θηλυκό, Number.Ενικός): Word(["μπύρα"], [1]),
    (Case.Ονομαστική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["μπύρες", "μπύραι"], [0.8, 0.2]),
    (Case.Γενική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["μπυρῶν"], [1]),
    (Case.Δοτική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["μπύραις"], [1]),
    (Case.Αιτιατική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["μπύρες", "μπύρας"], [0.8, 0.2]),
    (Case.Κλητική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["μπύρες", "μπύραι"], [0.8, 0.2]),
})

souvla = Noun({
    (Case.Ονομαστική, Gender.Θηλυκό, Number.Ενικός): Word(["σούβλα"], [1]),
    (Case.Γενική, Gender.Θηλυκό, Number.Ενικός): Word(["σούβλας"], [1]),
    (Case.Δοτική, Gender.Θηλυκό, Number.Ενικός): Word(["σούβλᾳ"], [1]),
    (Case.Αιτιατική, Gender.Θηλυκό, Number.Ενικός): Word(["σούβλαν", "σούβλα"], [0.2, 0.8]),
    (Case.Κλητική, Gender.Θηλυκό, Number.Ενικός): Word(["σούβλα"], [1]),
    (Case.Ονομαστική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["σούβλες", "σούβλαι"], [0.8, 0.2]),
    (Case.Γενική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["σουβλῶν"], [1]),
    (Case.Δοτική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["σούβλαις"], [1]),
    (Case.Αιτιατική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["σούβλες", "σούβλας"], [0.8, 0.2]),
    (Case.Κλητική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["σούβλες", "σούβλαι"], [0.8, 0.2]),
})

mpanana = Noun({
    (Case.Ονομαστική, Gender.Θηλυκό, Number.Ενικός): Word(["μπανάνα"], [1]),
    (Case.Γενική, Gender.Θηλυκό, Number.Ενικός): Word(["μπανάνας"], [1]),
    (Case.Δοτική, Gender.Θηλυκό, Number.Ενικός): Word(["μπανάνᾳ"], [1]),
    (Case.Αιτιατική, Gender.Θηλυκό, Number.Ενικός): Word(["μπανάναν", "μπανάνα"], [0.2, 0.8]),
    (Case.Κλητική, Gender.Θηλυκό, Number.Ενικός): Word(["μπανάνα"], [1]),
    (Case.Ονομαστική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["μπανάνες", "μπανάναι"], [0.8, 0.2]),
    (Case.Γενική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["μπανανῶν"], [1]),
    (Case.Δοτική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["μπανάναις"], [1]),
    (Case.Αιτιατική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["μπανάνες", "μπανάνας"], [0.8, 0.2]),
    (Case.Κλητική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["μπανάνες", "μπανάναι"], [0.8, 0.2]),
})

# Nouns/Neuter
milo = Noun({
    (Case.Ονομαστική, Gender.Ουδέτερο, Number.Ενικός): Word(["μῆλον", "μῆλο"], [0.5, 0.5]),
    (Case.Γενική, Gender.Ουδέτερο, Number.Ενικός): Word(["μῆλου"], [1]),
    (Case.Δοτική, Gender.Ουδέτερο, Number.Ενικός): Word(["μήλῳ"], [1]),
    (Case.Αιτιατική, Gender.Ουδέτερο, Number.Ενικός): Word(["μῆλον", "μῆλο"], [0.5, 0.5]),
    (Case.Κλητική, Gender.Ουδέτερο, Number.Ενικός): Word(["μῆλον", "μῆλο"], [0.5, 0.5]),
    (Case.Ονομαστική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["μῆλα"], [1]),
    (Case.Γενική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["μήλων"], [1]),
    (Case.Δοτική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["μήλοις"], [1]),
    (Case.Αιτιατική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["μῆλα"], [1]),
    (Case.Κλητική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["μῆλα"], [1]),
})

nero = Noun({
    (Case.Ονομαστική, Gender.Ουδέτερο, Number.Ενικός): Word(["νερόν", "νερό"], [0.5, 0.5]),
    (Case.Γενική, Gender.Ουδέτερο, Number.Ενικός): Word(["νεροῦ"], [1]),
    (Case.Δοτική, Gender.Ουδέτερο, Number.Ενικός): Word(["νερῷ"], [1]),
    (Case.Αιτιατική, Gender.Ουδέτερο, Number.Ενικός): Word(["νερόν", "νερό"], [0.5, 0.5]),
    (Case.Κλητική, Gender.Ουδέτερο, Number.Ενικός): Word(["νερόν", "νερό"], [0.5, 0.5]),
    (Case.Ονομαστική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["νερά"], [1]),
    (Case.Γενική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["νερῶν"], [1]),
    (Case.Δοτική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["νεροῖς"], [1]),
    (Case.Αιτιατική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["νερά"], [1]),
    (Case.Κλητική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["νερά"], [1]),
})

fai = Noun({
    (Case.Ονομαστική, Gender.Ουδέτερο, Number.Ενικός): Word(["φαΐ", "φαΐν", "φαγητό"], [0.3, 0.3, 0.4]),
    (Case.Γενική, Gender.Ουδέτερο, Number.Ενικός): Word(["φαγιοῦ", "φαγητοῦ"], [0.5, 0.5]),
    (Case.Δοτική, Gender.Ουδέτερο, Number.Ενικός): Word(["φαγητῷ"], [1]),
    (Case.Αιτιατική, Gender.Ουδέτερο, Number.Ενικός): Word(["φαΐ", "φαΐν", "φαγητό"], [0.3, 0.3, 0.4]),
    (Case.Κλητική, Gender.Ουδέτερο, Number.Ενικός): Word(["φαΐ", "φαΐν",  "φαγητό"], [0.3, 0.3, 0.4]),
    (Case.Ονομαστική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["φαγιά", "φαγητά"], [0.5, 0.5]),
    (Case.Γενική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["φαγιῶν", "φαγητῶν"], [0.5, 0.5]),
    (Case.Δοτική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["φαγητοῖς"], [1]),
    (Case.Αιτιατική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["φαγιά", "φαγητά"], [0.5, 0.5]),
    (Case.Κλητική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["φαγιά", "φαγητά"], [0.5, 0.5]),
})

poto = Noun({
    (Case.Ονομαστική, Gender.Ουδέτερο, Number.Ενικός): Word(["ποτόν", "ποτό"], [0.5, 0.5]),
    (Case.Γενική, Gender.Ουδέτερο, Number.Ενικός): Word(["ποτοῦ"], [1]),
    (Case.Δοτική, Gender.Ουδέτερο, Number.Ενικός): Word(["ποτῷ"], [1]),
    (Case.Αιτιατική, Gender.Ουδέτερο, Number.Ενικός): Word(["ποτόν", "ποτό"], [0.5, 0.5]),
    (Case.Κλητική, Gender.Ουδέτερο, Number.Ενικός): Word(["ποτόν", "ποτό"], [0.5, 0.5]),
    (Case.Ονομαστική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["ποτά"], [1]),
    (Case.Γενική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["ποτῶν"], [1]),
    (Case.Δοτική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["ποτοῖς"], [1]),
    (Case.Αιτιατική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["ποτά"], [1]),
    (Case.Κλητική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["ποτά"], [1]),
})

halloumi = Noun({
    (Case.Ονομαστική, Gender.Ουδέτερο, Number.Ενικός): Word(["χαλλούμιν", "χαλλούμι"], [0.5, 0.5]),
    (Case.Γενική, Gender.Ουδέτερο, Number.Ενικός): Word(["χαλλουμιοῦ"], [1]),
    (Case.Δοτική, Gender.Ουδέτερο, Number.Ενικός): Word(["χαλλουμίῳ"], [1]),
    (Case.Αιτιατική, Gender.Ουδέτερο, Number.Ενικός): Word(["χαλλούμιν", "χαλλούμι"], [0.5, 0.5]),
    (Case.Κλητική, Gender.Ουδέτερο, Number.Ενικός): Word(["χαλλούμιν", "χαλλούμι"], [0.5, 0.5]),
    (Case.Ονομαστική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["χαλλούμια"], [1]),
    (Case.Γενική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["χαλλουμιῶν"], [1]),
    (Case.Δοτική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["χλλουμίοις"], [1]),
    (Case.Αιτιατική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["χαλλούμια"], [1]),
    (Case.Κλητική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["χαλλούμια"], [1]),
})

nouns = [
    # Food / drink
    milo, nero, fai, poto, mpyra, halloumi, souvla, mpanana, karaolos,

    # Names
    Visos, Evripidis, Matthaios, Andrianos, Valentina
]

# Adjectives

polys = Adjective({
    (Case.Ονομαστική, Gender.Αρσενικό, Number.Ενικός): Word(["πολύς"], [1]),
    (Case.Γενική, Gender.Αρσενικό, Number.Ενικός): Word(["πολλοῦ"], [1]),
    (Case.Δοτική, Gender.Αρσενικό, Number.Ενικός): Word(["πολλῷ"], [1]),
    (Case.Αιτιατική, Gender.Αρσενικό, Number.Ενικός): Word(["πολύν"], [1]),
    (Case.Κλητική, Gender.Αρσενικό, Number.Ενικός): Word(["πολύ"], [1]),
    (Case.Ονομαστική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["πολλοί"], [1]),
    (Case.Γενική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["πολλῶν"], [1]),
    (Case.Δοτική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["πολλοῖς"], [1]),
    (Case.Αιτιατική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["πολλούς"], [1]),
    (Case.Κλητική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["πολλοί"], [1]),

    (Case.Ονομαστική, Gender.Θηλυκό, Number.Ενικός): Word(["πολλή"], [1]),
    (Case.Γενική, Gender.Θηλυκό, Number.Ενικός): Word(["πολλῆς"], [1]),
    (Case.Δοτική, Gender.Θηλυκό, Number.Ενικός): Word(["πολλῇ"], [1]),
    (Case.Αιτιατική, Gender.Θηλυκό, Number.Ενικός): Word(["πολλήν"], [1]),
    (Case.Κλητική, Gender.Θηλυκό, Number.Ενικός): Word(["πολλή"], [1]),
    (Case.Ονομαστική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["πολλές", "πολλαί"], [0.8, 0.2]),
    (Case.Γενική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["πολλῶν"], [1]),
    (Case.Δοτική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["πολλαῖς"], [1]),
    (Case.Αιτιατική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["πολλές", "πολλάς"], [0.8, 0.2]),
    (Case.Κλητική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["πολλές", "πολλαί"], [0.8, 0.2]),
    
    (Case.Ονομαστική, Gender.Ουδέτερο, Number.Ενικός): Word(["πολύ"], [1]),
    (Case.Γενική, Gender.Ουδέτερο, Number.Ενικός): Word(["πολλοῦ"], [1]),
    (Case.Δοτική, Gender.Ουδέτερο, Number.Ενικός): Word(["πολλῷ"], [1]),
    (Case.Αιτιατική, Gender.Ουδέτερο, Number.Ενικός): Word(["πολύ"], [1]),
    (Case.Κλητική, Gender.Ουδέτερο, Number.Ενικός): Word(["πολύ"], [1]),
    (Case.Ονομαστική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["πολλά"], [1]),
    (Case.Γενική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["πολλῶν"], [1]),
    (Case.Δοτική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["πολλοῖς"], [1]),
    (Case.Αιτιατική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["πολλά"], [1]),
    (Case.Κλητική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["πολλά"], [1]),
})

kalos = Adjective({
    (Case.Ονομαστική, Gender.Αρσενικό, Number.Ενικός): Word(["καλός"], [1]),
    (Case.Γενική, Gender.Αρσενικό, Number.Ενικός): Word(["καλοῦ"], [1]),
    (Case.Δοτική, Gender.Αρσενικό, Number.Ενικός): Word(["καλῷ"], [1]),
    (Case.Αιτιατική, Gender.Αρσενικό, Number.Ενικός): Word(["καλόν"], [1]),
    (Case.Κλητική, Gender.Αρσενικό, Number.Ενικός): Word(["καλέ"], [1]),
    (Case.Ονομαστική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["καλοί"], [1]),
    (Case.Γενική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["καλῶν"], [1]),
    (Case.Δοτική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["καλοῖς"], [1]),
    (Case.Αιτιατική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["καλούς"], [1]),
    (Case.Κλητική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["καλοί"], [1]),

    (Case.Ονομαστική, Gender.Θηλυκό, Number.Ενικός): Word(["καλή"], [1]),
    (Case.Γενική, Gender.Θηλυκό, Number.Ενικός): Word(["καλῆς"], [1]),
    (Case.Δοτική, Gender.Θηλυκό, Number.Ενικός): Word(["καλῇ"], [1]),
    (Case.Αιτιατική, Gender.Θηλυκό, Number.Ενικός): Word(["καλήν"], [1]),
    (Case.Κλητική, Gender.Θηλυκό, Number.Ενικός): Word(["καλή"], [1]),
    (Case.Ονομαστική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["καλές", "καλαί"], [0.8, 0.2]),
    (Case.Γενική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["καλῶν"], [1]),
    (Case.Δοτική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["καλαῖς"], [1]),
    (Case.Αιτιατική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["καλές", "καλαί"], [0.8, 0.2]),
    (Case.Κλητική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["καλές", "καλαί"], [0.8, 0.2]),
    
    (Case.Ονομαστική, Gender.Ουδέτερο, Number.Ενικός): Word(["καλόν", "καλό"], [0.5, 0.5]),
    (Case.Γενική, Gender.Ουδέτερο, Number.Ενικός): Word(["καλοῦ"], [1]),
    (Case.Δοτική, Gender.Ουδέτερο, Number.Ενικός): Word(["καλῷ"], [1]),
    (Case.Αιτιατική, Gender.Ουδέτερο, Number.Ενικός):  Word(["καλόν", "καλό"], [0.5, 0.5]),
    (Case.Κλητική, Gender.Ουδέτερο, Number.Ενικός):  Word(["καλόν", "καλό"], [0.5, 0.5]),
    (Case.Ονομαστική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["καλά"], [1]),
    (Case.Γενική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["καλῶν"], [1]),
    (Case.Δοτική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["καλοῖς"], [1]),
    (Case.Αιτιατική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["καλά"], [1]),
    (Case.Κλητική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["καλά"], [1]),
})

kakos = Adjective({
    (Case.Ονομαστική, Gender.Αρσενικό, Number.Ενικός): Word(["κακός"], [1]),
    (Case.Γενική, Gender.Αρσενικό, Number.Ενικός): Word(["κακοῦ"], [1]),
    (Case.Δοτική, Gender.Αρσενικό, Number.Ενικός): Word(["κακῷ"], [1]),
    (Case.Αιτιατική, Gender.Αρσενικό, Number.Ενικός): Word(["κακόν"], [1]),
    (Case.Κλητική, Gender.Αρσενικό, Number.Ενικός): Word(["κακέ"], [1]),
    (Case.Ονομαστική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["κακοί"], [1]),
    (Case.Γενική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["κακῶν"], [1]),
    (Case.Δοτική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["κακοῖς"], [1]),
    (Case.Αιτιατική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["κακούς"], [1]),
    (Case.Κλητική, Gender.Αρσενικό, Number.Πληθυντικός): Word(["κακοί"], [1]),

    (Case.Ονομαστική, Gender.Θηλυκό, Number.Ενικός): Word(["κακή"], [1]),
    (Case.Γενική, Gender.Θηλυκό, Number.Ενικός): Word(["κακῆς"], [1]),
    (Case.Δοτική, Gender.Θηλυκό, Number.Ενικός): Word(["κακῇ"], [1]),
    (Case.Αιτιατική, Gender.Θηλυκό, Number.Ενικός): Word(["κακήν"], [1]),
    (Case.Κλητική, Gender.Θηλυκό, Number.Ενικός): Word(["κακή"], [1]),
    (Case.Ονομαστική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["κακές", "κακαί"], [0.8, 0.2]),
    (Case.Γενική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["κακῶν"], [1]),
    (Case.Δοτική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["κακαῖς"], [1]),
    (Case.Αιτιατική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["κακές", "κακαί"], [0.8, 0.2]),
    (Case.Κλητική, Gender.Θηλυκό, Number.Πληθυντικός): Word(["κακές", "κακαί"], [0.8, 0.2]),
    
    (Case.Ονομαστική, Gender.Ουδέτερο, Number.Ενικός): Word(["κακόν", "κακό"], [0.5, 0.5]),
    (Case.Γενική, Gender.Ουδέτερο, Number.Ενικός): Word(["κακοῦ"], [1]),
    (Case.Δοτική, Gender.Ουδέτερο, Number.Ενικός): Word(["κακῷ"], [1]),
    (Case.Αιτιατική, Gender.Ουδέτερο, Number.Ενικός):  Word(["κακόν", "κακό"], [0.5, 0.5]),
    (Case.Κλητική, Gender.Ουδέτερο, Number.Ενικός):  Word(["κακόν", "κακό"], [0.5, 0.5]),
    (Case.Ονομαστική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["κακά"], [1]),
    (Case.Γενική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["κακῶν"], [1]),
    (Case.Δοτική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["κακοῖς"], [1]),
    (Case.Αιτιατική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["κακά"], [1]),
    (Case.Κλητική, Gender.Ουδέτερο, Number.Πληθυντικός): Word(["κακά"], [1]),
})

# Verbs

paizo = Verb({
    (Mood.Οριστική, Number.Ενικός, Person.Α, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["παίζω"], [1]),
    (Mood.Οριστική, Number.Ενικός, Person.Β, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["παίζεις"], [1]),
    (Mood.Οριστική, Number.Ενικός, Person.Γ, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["παίζει"], [1]),
    (Mood.Οριστική, Number.Πληθυντικός, Person.Α, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["παίζουμε", "παίζωμεν", "παίζουμεν"], [0.8, 0.1, 0.1]),
    (Mood.Οριστική, Number.Πληθυντικός, Person.Β, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["παίζετε"], [1]),
    (Mood.Οριστική, Number.Πληθυντικός, Person.Γ, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["παίζουν", "παίζουσιν", "παίζουσι"], [0.8, 0.1, 0.1]),
})

vlepo = Verb({
    (Mood.Οριστική, Number.Ενικός, Person.Α, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["βλέπω"], [1]),
    (Mood.Οριστική, Number.Ενικός, Person.Β, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["βλέπεις"], [1]),
    (Mood.Οριστική, Number.Ενικός, Person.Γ, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["βλέπει"], [1]),
    (Mood.Οριστική, Number.Πληθυντικός, Person.Α, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["βλέπουμε", "βλέπωμεν", "βλέπουμεν"], [0.8, 0.1, 0.1]),
    (Mood.Οριστική, Number.Πληθυντικός, Person.Β, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["βλέπετε"], [1]),
    (Mood.Οριστική, Number.Πληθυντικός, Person.Γ, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["βλέπουν", "βλέπουσιν", "βλέπουσι"], [0.8, 0.1, 0.1]),
})

troo = Verb({
    (Mood.Οριστική, Number.Ενικός, Person.Α, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["τρώω", "τρώγω"], [0.5, 0.5]),
    (Mood.Οριστική, Number.Ενικός, Person.Β, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["τρώεις", "τρῶς"], [0.5, 0.5]),
    (Mood.Οριστική, Number.Ενικός, Person.Γ, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["τρώει"], [1]),
    (Mood.Οριστική, Number.Πληθυντικός, Person.Α, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["τρῶμεν", "τρώγωμεν", "τρῶμε"], [0.3, 0.3, 0.4]),
    (Mood.Οριστική, Number.Πληθυντικός, Person.Β, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["τρῶτε", "τρώγετε"], [0.5, 0.5]),
    (Mood.Οριστική, Number.Πληθυντικός, Person.Γ, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["τρῶνε", "τρώγουσι", "τρώσιν"], [0.3, 0.3, 0.4]),
})

eimai = Verb({
    (Mood.Οριστική, Number.Ενικός, Person.Α, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["εἶμαι", "εἰμί"], [0.9, 0.1]),
    (Mood.Οριστική, Number.Ενικός, Person.Β, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["εἶσαι", "εἶ"], [0.9, 0.1]),
    (Mood.Οριστική, Number.Ενικός, Person.Γ, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["εἶναι", "ἔνι", "ἐστί"], [0.45, 0.45, 0.1]),
    (Mood.Οριστική, Number.Πληθυντικός, Person.Α, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["εἴμαστεν", "εἴμαστε", "ἐσμέν"], [0.45, 0.45, 0.1]),
    (Mood.Οριστική, Number.Πληθυντικός, Person.Β, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["εἴσαστεν", "εἴσαστε", "εἶστε", "ἐστέ"], [0.3, 0.3, 0.3, 0.1]),
    (Mood.Οριστική, Number.Πληθυντικός, Person.Γ, Tense.Ενεστώτας, Voice.Ενεργητική): Word(["εἶναι", "ἔνουσιν", "ἔνι", "εἰσί"], [0.45, 0.1, 0.35, 0.1]),
}, katigoroumeno=True)

# Adverbs declared in main

grammar_to_str = {
    Mood.Οριστική: "oristiki",
    Mood.Ευκτική: "eyktiki",
    Mood.Προστακτική: "prostaktiki",
    Mood.Υποτακτική: "ypotaktiki",

    Number.Ενικός: "enikos",
    Number.Δυϊκός: "dyikos",
    Number.Πληθυντικός: "plithyntikos",

    Person.Α: "A",
    Person.Β: "B",
    Person.Γ: "C",

    Tense.Αόριστος: "aoristos",
    Tense.Ενεστώτας: "enestotas",
    Tense.Παρατατικός: "paratatikos",
    Tense.Παρακείμενος: "parakeimenos",
    Tense.ΜέλλονταςΕξακολουθητηκός: "mellontasEx",
    Tense.ΜέλλονταςΣυντελεσμένος: "mellontasSyn",
    
    Gender.Αρσενικό: "arseniko",
    Gender.Θηλυκό: "thilyko",
    Gender.Ουδέτερο: "oydetero",

    Voice.Ενεργητική: "energitiki",
    Voice.Μέση: "mesi",
    Voice.Παθητική: "pathitiki",

    Case.Ονομαστική: "onomastiki",
    Case.Γενική: "geniki",
    Case.Δοτική: "dotiki",
    Case.Αιτιατική: "aitiatiki",
    Case.Κλητική: "klitiki"
}

def string_from_tuple(prefix, t: Tuple) -> str:
    M = len(t)
    ret = prefix
    for i in range(M):
        ret += "#" + grammar_to_str[t[i]]
    return ret

def convert_lists_to_saveable(verbs: List[Verb], adjectives: List[Adjective], nouns: List[Noun]):
    verbs: List[VerbConjugationDict] = [v.conjugation_dict for v in verbs]
    adjectives: List[AdjectiveDeclensionDict] = [a.declension_dict for a in adjectives]
    nouns: List[NounDeclensionDict] = [n.declension_dict for n in nouns]

    verbs = [{string_from_tuple('verb', verbForm): (word.words, word.probabilities) for verbForm, word in verb.items()} for verb in verbs]
    adjectives = [{string_from_tuple('adjective', adjectiveForm): [word.words, word.probabilities] for adjectiveForm, word in adjective.items()} for adjective in adjectives]
    nouns = [{string_from_tuple(f'noun#{noun.kyrio}', nounForm): [word.words, word.probabilities] for nounForm, word in noun.items()} for noun in nouns]
    return verbs, adjectives, nouns

if __name__ == "__main__":
    verbs = [
        paizo, vlepo, troo, eimai
    ]
    adjectives = [
        polys, kalos, kakos
    ]
    nouns = [
        # Food / drink
        milo, nero, fai, poto, mpyra, halloumi, souvla, mpanana, karaolos,

        # Names
        Visos, Evripidis, Matthaios, Andrianos, Valentina
    ]
    adverbs = ["καλῶς", "κακῶς", "καλά", "κακά", "γρήγορα", "αργά"]

    verbs, adjectives, nouns = convert_lists_to_saveable(verbs, adjectives, nouns)
    print(nouns)

    nouns_filename = "data/glossarion/ousiastika.npy"
    adjectives_filename = "data/glossarion/epitheta.npy"
    verbs_filename = "data/glossarion/rimata.npy"
    adverbs_filename = "data/glossarion/epirrimata.npy"

    with open(nouns_filename, "wb") as f:
        np.save(f, nouns)
    with open(adjectives_filename, "wb") as f:
        np.save(f, adjectives)
    with open(verbs_filename, "wb") as f:
        np.save(f, verbs)
    with open(adverbs_filename, "wb") as f:
        np.save(f, adverbs)