import spacy
from spacy.language import Language
# from ..models import taskModel
from spacy.matcher import PhraseMatcher, Matcher
from spacy.tokens import Span

# this uses POS and Regular expressions type syntax to match call in a sentence.


class nlpExtractor:
    def __init__(self):
        self.training_data = []
        self.communicateIntentVocab = ['discuss', 'call', 'telephone', 'phone call', 'phone', 'ring', 'coverse',
                                       'conversation', 'talk', 'meet', 'meeting', 'conference', 'concall', 'video call', 'speak', 'connect with', 'skype', 'whatsapp', 'dm', 'pm', 'message', 'reply', 'mail', 'email', 'voice call']

        @Language.component("isCallAction")
        def isCallAction(doc):
            commMatches = self.commMatcher(doc)
            commSpans = [Span(doc, start, end, label="PhoneCall")
                         for matchId, start, end in commMatches]
            # print(commSpans)

            self.training_data.append(
                [(spans.start_char, spans.end_char, spans.label_) for spans in commSpans])
            doc.ents = commSpans
            return doc

        @Language.component("isLearningAction")
        def isLearningAction(doc):
            pass

    def extractObjectAndAction(self, textToExtractFrom):
        nlp = spacy.load("en_core_web_md")
        # allStopWords = nlp.Defaults.stop_words
        doc = nlp(textToExtractFrom)
        print([(token.text, token.dep_, token.pos_)
              for token in doc])

    def matchPatternsForCall(self, taskText):
        nlp = spacy.load("en_core_web_md")
        self.commMatcher = Matcher(nlp.vocab)
        commPatterns = [{'LOWER': {'IN': self.communicateIntentVocab}}, {
            "LOWER": "to", "OP": "?"}, {"LOWER": "with", "OP": "?"}, {"POS": "PROPN"}]

        self.commMatcher.add("PhoneCall", [commPatterns])
        nlp.add_pipe('isCallAction', last=True)
        doc = nlp(taskText)
        resultToSend = [x for x in doc.ents if x.label_ == "PhoneCall"]
        return resultToSend

    def matchPatternsForLearning(self, taskText):

        pass
