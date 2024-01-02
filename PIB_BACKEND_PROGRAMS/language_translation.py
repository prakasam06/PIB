from googletrans import Translator

def language_translation(input_string,source_lan,target_lag):
    language = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
    googletrans_translator = Translator()
    googletrans_result = googletrans_translator.translate(input_string,src= "auto", dest= language[target_lag])
    return googletrans_result.text

print(language_translation("విద్యావ్యవస్థను బలోపేతం చేసిసమస్యలను పరిష్కరించాలి:ఎస్టీయూటీఎస్ హైదరాబాద్ జిల్లా అధ్యక్షులు ఇఫ్తికారుద్దీన్హైదరాబాద్;, 08 డిసెంబర్ (ఆదాబ్ హైదరాబాద్):విద్యావ్యకనిర్వీర్యపోయిందని:ఇన్నాళ్లస్యలను అస్గంచుకోదనిఅందువలకొత్తగా కొలువుదీరినభుత్వంంశాలపైపెట్టాలనిస్టియూటిఎస్రాబ్దాద్ జిల్లా అధ్యక్షులు ఇఫ్తికారుద్దీన్;ధానంమసుబాఅన్నాతెలంగాణముఖ్యమంత్రిగాబాధ్యతలుచెపసీఎంరెవంత్రెడ్డికిభాకాంక్షలుతెలిపారు0గా వారు మాటాడుతూవిదాాఅనేకసవాళ్లుసమస్యలుఉన్నప్పటికీగతతాలుంచుకునదాఖలాలు71711ఉపాధ్యాయ పోస్టులభరిలుఎనొఏళ్లుగా నిలిచిపోయాయన్నారు   పీఈపండితుల   అప్గ్రేడేషన్ప్రమోషన్ల ప్రక్రియకూడాచానాళ్లుగాఆగిపోయిందననారుఎల్ఎఫ్ఎన్:హెచ్ఎం పోస్టులను వెంటనే భర్తీ చేయాలని కొత్త07గాా7- 'టీచర్ల -ష్రంలోటీచర్ల్లుసందర్భంసలోపైమరీ","english","english"))


