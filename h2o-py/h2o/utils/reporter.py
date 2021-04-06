import sys
import uuid

from humbug.consent import HumbugConsent
from humbug.report import Reporter, Modes

HUMBUG_TOKEN = ""
HUMBUG_KB_ID = ""

session_id = str(uuid.uuid4())
session_id_tag = "session_id:{}".format(session_id)


h2o_tags = ["123"]

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

)

def setup_excepthook():
    h2o_reporter.system_report(publish=True, tags=h2o_tags)
    try:
        ipython_shell = get_ipython()
        old_showtraceback = ipython_shell.showtraceback
        def showtraceback(*args, **kwargs):
            _, exc_instance, _ = sys.exc_info()
            h2o_reporter.error_report(exc_instance, tags=h2o_tags, publish=True)
            old_showtraceback(*args, **kwargs)

        ipython_shell.showtraceback = showtraceback
    except NameError:
        h2o_reporter.setup_excepthook(publish=True, tags=h2o_tags)
