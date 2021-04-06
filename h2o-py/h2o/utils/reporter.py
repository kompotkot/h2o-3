import uuid

from .version import __version__

from humbug.consent import HumbugConsent
from humbug.report import Reporter, Modes

HUMBUG_TOKEN = ""
HUMBUG_KB_ID = ""

session_id = str(uuid.uuid4())
session_id_tag = "session_id:{}".format(session_id)


h2o_tags = [__version__]


class ConsentState:
    def __init__(self, consent: bool = False) -> None:
        self.consent: bool = consent

    def check(self) -> bool:
        return self.consent


h2o_consent_state = ConsentState(True)

h2o_consent = HumbugConsent(h2o_consent_state.check)
h2o_reporter = Reporter(
    name="h2o",
    consent=h2o_consent,
    client_id=None,
    session_id=session_id,
    bugout_token=HUMBUG_TOKEN,
    bugout_journal_id=HUMBUG_KB_ID,
    mode=Modes.DEFAULT,
)
notebook_reporter = h2o_reporter.setup_notebook_excepthook(tags=h2o_tags)
