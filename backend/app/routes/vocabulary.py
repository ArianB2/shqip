from fastapi import APIRouter, HTTPException, Query
from typing import Literal

router = APIRouter()

# ---------------------------------------------------------------------------
# Real Albanian vocabulary — Gheg & Tosk variants.
# Data sourced from Arian's personal vocabulary spreadsheet.
#
# Month 2: migrate this into PostgreSQL on Amazon RDS.
# Month 3: wire each word to Amazon Polly for audio.
# ---------------------------------------------------------------------------

VOCABULARY = {

    # ── Subject Pronouns ───────────────────────────────────────────────────
    "subject_pronouns": [
        {"id": 1,  "english": "I",                      "tosk": "unë",         "gheg": "unë",              "notes": "Identical in both dialects"},
        {"id": 2,  "english": "you (singular)",          "tosk": "ti",          "gheg": "ti",               "notes": "Identical in both dialects"},
        {"id": 3,  "english": "he",                      "tosk": "ai",          "gheg": "ai",               "notes": "Identical in both dialects"},
        {"id": 4,  "english": "she",                     "tosk": "ajo",         "gheg": "ajo",              "notes": "Identical in both dialects"},
        {"id": 5,  "english": "we",                      "tosk": "ne",          "gheg": "na",               "notes": "Gheg uses 'na' — one of the most common dialect differences"},
        {"id": 6,  "english": "you (plural / formal)",   "tosk": "ju",          "gheg": "ju",               "notes": "Identical in both dialects"},
        {"id": 7,  "english": "they (masculine / mixed)","tosk": "ata",         "gheg": "ata",              "notes": "Identical in both dialects"},
        {"id": 8,  "english": "they (feminine)",         "tosk": "ato",         "gheg": "ato",              "notes": "Identical in both dialects"},
    ],

    # ── Object Pronouns ────────────────────────────────────────────────────
    "object_pronouns": [
        {"id": 9,  "english": "me",       "tosk": "më",    "gheg": "mu",    "notes": "Clear Gheg vs Tosk difference — Gheg uses 'mu'"},
        {"id": 10, "english": "you",      "tosk": "të",    "gheg": "ty",    "notes": "Gheg uses 'ty'"},
        {"id": 11, "english": "him / her","tosk": "e / i", "gheg": "e / i", "notes": "Identical in both dialects"},
        {"id": 12, "english": "us",       "tosk": "na",    "gheg": "na",    "notes": "Identical in both dialects"},
        {"id": 13, "english": "them",     "tosk": "i",     "gheg": "i",     "notes": "Identical in both dialects"},
    ],

    # ── Possessive Pronouns ────────────────────────────────────────────────
    "possessive_pronouns": [
        {"id": 14, "english": "my",   "tosk": "im / ime", "gheg": "jem / jeme", "notes": "Gheg uses 'jem/jeme' — very common in everyday Gheg speech"},
        {"id": 15, "english": "your", "tosk": "yt / jote", "gheg": "jot / jote","notes": "Gheg 'jot' vs Tosk 'yt' for masculine form"},
        {"id": 16, "english": "his",  "tosk": "i tij",    "gheg": "i tij",      "notes": "Identical in both dialects"},
        {"id": 17, "english": "her",  "tosk": "i saj",    "gheg": "i saj",      "notes": "Identical in both dialects"},
        {"id": 18, "english": "our",  "tosk": "ynë",      "gheg": "jonë",       "notes": "Gheg 'jonë' vs Tosk 'ynë' — a hallmark dialect difference"},
        {"id": 19, "english": "their","tosk": "i tyne",   "gheg": "i tyre",     "notes": "Slight vowel difference between dialects"},
    ],

    # ── Greetings & Basics ─────────────────────────────────────────────────
    "greetings": [
        {"id": 20, "english": "hello",         "tosk": "përshëndetje",    "gheg": "tung",               "notes": "Gheg 'tung' is much shorter and more casual — widely used in Kosovo"},
        {"id": 21, "english": "hi",            "tosk": "përshëndetje",    "gheg": "hej / përshëndetje", "notes": "Gheg speakers often use 'hej' informally"},
        {"id": 22, "english": "good morning",  "tosk": "mirëmëngjes",     "gheg": "mirëmëngjes",        "notes": "Identical in both dialects"},
        {"id": 23, "english": "good afternoon","tosk": "mirëdita",        "gheg": "mirëdita",           "notes": "Identical in both dialects"},
        {"id": 24, "english": "good evening",  "tosk": "mirëmbrëma",      "gheg": "mirëmbrëma",         "notes": "Identical in both dialects"},
        {"id": 25, "english": "good night",    "tosk": "natën e mirë",    "gheg": "natën e mirë",       "notes": "Identical in both dialects"},
        {"id": 26, "english": "goodbye",       "tosk": "mirupafshim",     "gheg": "mirupafshim",        "notes": "Identical in both dialects"},
        {"id": 27, "english": "see you later", "tosk": "shihemi më vonë", "gheg": "shihemi ma vonë",    "notes": "Gheg uses 'ma' where Tosk uses 'më' — a very common pattern"},
        {"id": 28, "english": "please",        "tosk": "të lutem",        "gheg": "t'lutna",            "notes": "Gheg form is contracted and sounds quite different"},
        {"id": 29, "english": "thank you",     "tosk": "faleminderit",    "gheg": "faleminderit",       "notes": "Identical in both dialects"},
        {"id": 30, "english": "thanks a lot",  "tosk": "shumë faleminderit","gheg": "shumë faleminderit","notes": "Identical in both dialects"},
        {"id": 31, "english": "excuse me",     "tosk": "më fal",          "gheg": "fal",                "notes": "Gheg drops the 'më' prefix — shorter and more direct"},
        {"id": 32, "english": "sorry",         "tosk": "më fal",          "gheg": "m'fal",              "notes": "Gheg contracts 'më fal' to 'm'fal'"},
        {"id": 33, "english": "no problem",    "tosk": "s'ka problem",    "gheg": "s'ka problem",       "notes": "Identical in both dialects"},
        {"id": 34, "english": "welcome",       "tosk": "mirë se vjen",    "gheg": "mirë se vjen",       "notes": "Identical in both dialects"},
        {"id": 35, "english": "yes",           "tosk": "po",              "gheg": "po",                 "notes": "Identical in both dialects"},
        {"id": 36, "english": "no",            "tosk": "jo",              "gheg": "jo",                 "notes": "Identical in both dialects"},
        {"id": 37, "english": "okay",          "tosk": "në rregull",      "gheg": "në rregull",         "notes": "Identical in both dialects"},
        {"id": 38, "english": "of course",     "tosk": "sigurisht",       "gheg": "normal",             "notes": "Gheg uses 'normal' — completely different word from Tosk"},
        {"id": 39, "english": "maybe",         "tosk": "ndoshta",         "gheg": "nashta",             "notes": "Gheg 'nashta' is a contracted informal form"},
    ],

    # ── Introductions ──────────────────────────────────────────────────────
    "introductions": [
        {"id": 40, "english": "what is your name?",       "tosk": "si e ke emrin?",       "gheg": "qysh e ki emrin?",       "notes": "Gheg uses 'qysh' (how/what) where Tosk uses 'si'"},
        {"id": 41, "english": "my name is",               "tosk": "emri im është",         "gheg": "emri jem osht",          "notes": "Gheg: 'jem' (my), 'osht' (is) — both differ from Tosk"},
        {"id": 42, "english": "where are you from?",      "tosk": "nga je?",               "gheg": "prej kah je?",           "notes": "Gheg 'prej kah' sounds very different from Tosk 'nga'"},
        {"id": 43, "english": "I am from",                "tosk": "jam nga",               "gheg": "jom prej",               "notes": "Gheg 'jom' vs Tosk 'jam', and 'prej' vs 'nga'"},
        {"id": 44, "english": "where do you live?",       "tosk": "ku jeton?",             "gheg": "ku jeton?",              "notes": "Identical in both dialects"},
        {"id": 45, "english": "I live in",                "tosk": "jetoj në",              "gheg": "jetoj n'",               "notes": "Gheg contracts 'në' to 'n'' before vowels"},
        {"id": 46, "english": "how old are you?",         "tosk": "sa vjeç je?",           "gheg": "sa vjeç je?",            "notes": "Identical in both dialects"},
        {"id": 47, "english": "I am ___ years old",       "tosk": "jam ___ vjeç",          "gheg": "jom ___ vjeç",           "notes": "Gheg 'jom' vs Tosk 'jam'"},
        {"id": 48, "english": "what is your phone number?","tosk": "cili është numri yt?", "gheg": "cili osht numri yt?",    "notes": "Gheg 'osht' vs Tosk 'është' — very common verb difference"},
        {"id": 49, "english": "my number is",             "tosk": "numri im është",        "gheg": "numri jem osht",         "notes": "Both 'my' and 'is' differ between dialects"},
        {"id": 50, "english": "how long have you been here?","tosk": "sa kohë je këtu?",   "gheg": "sa kohë je ktu?",        "notes": "Gheg drops the 'ë' in 'këtu' → 'ktu'"},
        {"id": 51, "english": "are you working?",         "tosk": "a po punon?",           "gheg": "a je tu punu?",          "notes": "Gheg uses 'je tu + infinitive' for present continuous"},
        {"id": 52, "english": "what do you do?",          "tosk": "çfarë bën?",            "gheg": "çka bon?",               "notes": "Gheg 'çka' vs Tosk 'çfarë', and 'bon' vs 'bën'"},
        {"id": 53, "english": "I work as",                "tosk": "punoj si",              "gheg": "punoj si",               "notes": "Identical in both dialects"},
        {"id": 54, "english": "are you married?",         "tosk": "a je i martuar?",       "gheg": "a je i martum?",         "notes": "Gheg drops the final syllable: 'martum' vs 'martuar'"},
        {"id": 55, "english": "I am married",             "tosk": "jam i martuar",         "gheg": "jom i martum",           "notes": "Both 'I am' and 'married' differ between dialects"},
        {"id": 56, "english": "I am single",              "tosk": "jam beqar",             "gheg": "jom beqar",              "notes": "Only 'jam/jom' differs"},
        {"id": 57, "english": "do you have children?",    "tosk": "a ke fëmijë?",          "gheg": "a ki fmi?",              "notes": "Gheg heavily contracts 'fëmijë' → 'fmi', and 'ke' → 'ki'"},
        {"id": 58, "english": "how many children?",       "tosk": "sa fëmijë ke?",         "gheg": "sa fmi ki?",             "notes": "Same contractions as above"},
        {"id": 59, "english": "this is my friend",        "tosk": "ky është shoku im",     "gheg": "ky osht shoku jem",      "notes": "'është/osht' and 'im/jem' both differ"},
        {"id": 60, "english": "this is my wife",          "tosk": "kjo është gruaja ime",  "gheg": "kjo osht gruaja jem",    "notes": "Same pattern — 'osht' and 'jem' in Gheg"},
        {"id": 61, "english": "this is my husband",       "tosk": "ky është burri im",     "gheg": "ky osht burri jem",      "notes": "Same pattern"},
        {"id": 62, "english": "nice to meet you",         "tosk": "mirë që u njohëm",      "gheg": "mirë që u njofëm",       "notes": "Gheg 'njofëm' vs Tosk 'njohëm'"},
        {"id": 63, "english": "likewise",                 "tosk": "gjithashtu",            "gheg": "gjithashtu",             "notes": "Identical in both dialects"},
        {"id": 64, "english": "welcome here",             "tosk": "mirë se erdhe",         "gheg": "mirë se erdhe",          "notes": "Identical in both dialects"},
    ],

    # ── Language Learning Phrases ──────────────────────────────────────────
    "language_phrases": [
        {"id": 65, "english": "I speak a little Albanian", "tosk": "flas pak shqip",             "gheg": "foli pak shqip",             "notes": "Gheg 'foli' vs Tosk 'flas'"},
        {"id": 66, "english": "I don't understand",        "tosk": "nuk kuptoj",                 "gheg": "s'po kuptoj",                "notes": "Gheg uses 's'po' as negation for present continuous"},
        {"id": 67, "english": "what does this mean?",      "tosk": "çfarë do të thotë kjo?",     "gheg": "çka domethan kjo?",          "notes": "Completely different phrasing — Gheg is much more compact"},
        {"id": 68, "english": "can you repeat?",           "tosk": "a mund të përsërisësh?",     "gheg": "a munesh me përsërit?",      "notes": "Gheg 'munesh me + infinitive' vs Tosk 'mund të + subjunctive'"},
        {"id": 69, "english": "speak slowly",              "tosk": "fol më ngadalë",             "gheg": "fol ma ngadalë",             "notes": "Gheg 'ma' vs Tosk 'më'"},
        {"id": 70, "english": "please write it",           "tosk": "shkruaje",                  "gheg": "shkruje",                    "notes": "Gheg drops a syllable: 'shkruje' vs 'shkruaje'"},
        {"id": 71, "english": "how do you say?",           "tosk": "si thuhet?",                "gheg": "qysh thuhet?",               "notes": "Gheg 'qysh' vs Tosk 'si' — a signature Gheg word"},
        {"id": 72, "english": "how do you spell it?",      "tosk": "si shkruhet?",              "gheg": "qysh shkruhet?",             "notes": "Same 'qysh/si' pattern"},
        {"id": 73, "english": "can you help me?",          "tosk": "a mund të më ndihmosh?",    "gheg": "a munesh me m'ndihmua?",     "notes": "Gheg infinitive construction vs Tosk subjunctive"},
        {"id": 74, "english": "I am learning Albanian",    "tosk": "po mësoj shqip",            "gheg": "jom tu mësu shqip",          "notes": "Gheg 'jom tu mësu' — the 'tu + infinitive' present continuous"},
        {"id": 75, "english": "I am a beginner",           "tosk": "jam fillestar",             "gheg": "jom fillestar",              "notes": "Only 'jam/jom' differs"},
        {"id": 76, "english": "one more time",             "tosk": "edhe një herë",             "gheg": "edhe ni herë",               "notes": "Gheg 'ni' vs Tosk 'një' for 'one' — very common difference"},
        {"id": 77, "english": "slower please",             "tosk": "më ngadalë ju lutem",       "gheg": "ma ngadalë ju lutem",        "notes": "Gheg 'ma' vs Tosk 'më'"},
        {"id": 78, "english": "I forgot",                  "tosk": "e harrova",                 "gheg": "e harrova",                  "notes": "Identical in both dialects"},
        {"id": 79, "english": "I remember",                "tosk": "e mbaj mend",               "gheg": "e maj men",                  "notes": "Gheg contracts 'mbaj mend' → 'maj men'"},
        {"id": 80, "english": "what is this?",             "tosk": "çfarë është kjo?",          "gheg": "çka osht kjo?",              "notes": "Both 'what' and 'is' differ — classic Gheg vs Tosk"},
        {"id": 81, "english": "what is that?",             "tosk": "çfarë është ajo?",          "gheg": "çka osht ajo?",              "notes": "Same pattern as above"},
        {"id": 82, "english": "who is that?",              "tosk": "kush është ai?",            "gheg": "kush osht ai?",              "notes": "Only 'është/osht' differs"},
        {"id": 83, "english": "where is the bathroom?",    "tosk": "ku është banja?",           "gheg": "ku osht banjo?",             "notes": "Gheg uses 'banjo', Tosk uses 'banja'"},
        {"id": 84, "english": "where is the restaurant?",  "tosk": "ku është restoranti?",      "gheg": "ku osht restoranti?",        "notes": "Only 'është/osht' differs"},
    ],

    # ── Common Verbs ───────────────────────────────────────────────────────
    "verbs": [
        {"id": 85,  "english": "to be",           "tosk": "të jem",      "gheg": "me kon",    "notes": "Completely different infinitive forms — one of the biggest Gheg/Tosk differences"},
        {"id": 86,  "english": "to have",          "tosk": "të kem",      "gheg": "me pas",    "notes": "Different infinitive forms"},
        {"id": 87,  "english": "to do / to make",  "tosk": "të bëj",      "gheg": "me bo",     "notes": "Gheg 'me bo' is much shorter — used for both 'do' and 'make'"},
        {"id": 88,  "english": "to go",            "tosk": "të shkosh",   "gheg": "me shku",   "notes": "Very different forms — memorize both"},
        {"id": 89,  "english": "to come",          "tosk": "të vish",     "gheg": "me ardhë",  "notes": "Gheg infinitive 'me ardhë' vs Tosk subjunctive 'të vish'"},
        {"id": 90,  "english": "to see",           "tosk": "të shohësh",  "gheg": "me pa",     "notes": "Gheg 'me pa' is very short compared to Tosk"},
        {"id": 91,  "english": "to know",          "tosk": "të dish",     "gheg": "me ditë",   "notes": "Similar roots, different forms"},
        {"id": 92,  "english": "to take",          "tosk": "të marrësh",  "gheg": "me marrë",  "notes": "Gheg uses infinitive, Tosk uses subjunctive"},
        {"id": 93,  "english": "to give",          "tosk": "të japësh",   "gheg": "me dhanë",  "notes": "Gheg 'me dhanë' — quite different from Tosk"},
        {"id": 94,  "english": "to find",          "tosk": "të gjesh",    "gheg": "me gjetë",  "notes": "Similar roots"},
        {"id": 95,  "english": "to think",         "tosk": "të mendosh",  "gheg": "me mendu",  "notes": "Gheg drops the final syllable: 'mendu' vs 'mendosh'"},
        {"id": 96,  "english": "to tell / show",   "tosk": "të tregosh",  "gheg": "me tregu",  "notes": "Same pattern — Gheg contracts the ending"},
        {"id": 97,  "english": "to work",          "tosk": "të punosh",   "gheg": "me punu",   "notes": "Gheg infinitive ending in '-u' is very common"},
        {"id": 98,  "english": "to call",          "tosk": "të thërrasësh","gheg": "me thirrë","notes": "Gheg 'me thirrë' is much simpler"},
        {"id": 99,  "english": "to try",           "tosk": "të provosh",  "gheg": "me provu",  "notes": "Gheg contracts '-osh' → '-u'"},
        {"id": 100, "english": "to ask",           "tosk": "të pyesësh",  "gheg": "me pytë",   "notes": "Different forms"},
        {"id": 101, "english": "to feel",          "tosk": "të ndjesh",   "gheg": "me ndi",    "notes": "Gheg 'me ndi' is very short"},
        {"id": 102, "english": "to become",        "tosk": "të bëhesh",   "gheg": "me u bo",   "notes": "Gheg reflexive uses 'u' particle"},
        {"id": 103, "english": "to leave",         "tosk": "të lësh",     "gheg": "me lanë",   "notes": "Different forms"},
        {"id": 104, "english": "to put",           "tosk": "të vësh",     "gheg": "me vu",     "notes": "Gheg 'me vu' is very compact"},
        {"id": 105, "english": "to hold / keep",   "tosk": "të mbash",    "gheg": "me majtë",  "notes": "Gheg 'me majtë' — different root from Tosk"},
        {"id": 106, "english": "to start",         "tosk": "të fillosh",  "gheg": "me fillu",  "notes": "Same root, Gheg contracts ending"},
        {"id": 107, "english": "to seem",          "tosk": "të dukesh",   "gheg": "me u dokë", "notes": "Gheg reflexive form with 'u'"},
        {"id": 108, "english": "to help",          "tosk": "të ndihmosh", "gheg": "me ndihmu", "notes": "Same root, Gheg contracts ending"},
        {"id": 109, "english": "to speak",         "tosk": "të flasësh",  "gheg": "me fol",    "notes": "Gheg 'me fol' — much shorter"},
        {"id": 110, "english": "to return",        "tosk": "të kthesh",   "gheg": "me kthy",   "notes": "Similar roots"},
        {"id": 111, "english": "to begin",         "tosk": "të nisësh",   "gheg": "me nis",    "notes": "Gheg drops the subjunctive ending"},
        {"id": 112, "english": "to live",          "tosk": "të jetosh",   "gheg": "me jetu",   "notes": "Same root, Gheg contracts"},
        {"id": 113, "english": "to believe",       "tosk": "të besosh",   "gheg": "me besu",   "notes": "Same root, Gheg contracts"},
        {"id": 114, "english": "to bring",         "tosk": "të sjellësh", "gheg": "me pru",    "notes": "Completely different roots — memorize both"},
        {"id": 115, "english": "to happen",        "tosk": "të ndodhë",   "gheg": "me ndodhë", "notes": "Very similar — only the prefix differs"},
        {"id": 116, "english": "to write",         "tosk": "të shkruash", "gheg": "me shkru",  "notes": "Same root, Gheg contracts"},
        {"id": 117, "english": "to read",          "tosk": "të lexosh",   "gheg": "me lexu",   "notes": "Same root, Gheg contracts"},
        {"id": 118, "english": "to learn",         "tosk": "të mësosh",   "gheg": "me mësu",   "notes": "Same root, Gheg contracts — important verb for this app!"},
        {"id": 119, "english": "to sit",           "tosk": "të ulesh",    "gheg": "me u ulë",  "notes": "Gheg uses reflexive 'u' particle"},
        {"id": 120, "english": "to stand / stay",  "tosk": "të qëndrosh", "gheg": "me qëndru", "notes": "Same root, Gheg contracts"},
        {"id": 121, "english": "to lose",          "tosk": "të humbësh",  "gheg": "me hup",    "notes": "Gheg 'me hup' — different from Tosk"},
        {"id": 122, "english": "to pay",           "tosk": "të paguash",  "gheg": "me pagu",   "notes": "Same root, Gheg contracts"},
        {"id": 123, "english": "to meet",          "tosk": "të takosh",   "gheg": "me taku",   "notes": "Same root, Gheg contracts"},
    ],
}


# ── Routes ─────────────────────────────────────────────────────────────────

@router.get("/categories")
def get_categories():
    """List all vocabulary categories with word counts."""
    return {
        "categories": [
            {
                "id": key,
                "label": key.replace("_", " ").title(),
                "word_count": len(words)
            }
            for key, words in VOCABULARY.items()
        ]
    }


@router.get("")
def get_vocabulary(
    category: str = Query(default="greetings", description="Vocabulary category"),
    dialect: Literal["gheg", "tosk"] = Query(default="tosk"),
):
    """
    Return vocabulary words for a given category.
    Both Gheg and Tosk forms are always returned so the UI
    can show comparisons regardless of which dialect is selected.
    """
    words = VOCABULARY.get(category)
    if not words:
        raise HTTPException(
            status_code=404,
            detail=f"Category '{category}' not found. Available: {list(VOCABULARY.keys())}"
        )
    return {
        "dialect": dialect,
        "category": category,
        "word_count": len(words),
        "words": words,
    }


@router.get("/{word_id}")
def get_word(word_id: int):
    """Return a single word by its ID — useful for quiz and flashcard features in Month 2."""
    for words in VOCABULARY.values():
        for word in words:
            if word["id"] == word_id:
                return word
    raise HTTPException(status_code=404, detail=f"Word with id {word_id} not found")
