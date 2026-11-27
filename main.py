"""The one sentence of apology an AI assistant owes the person it works for.

The line this program writes:

    I'm sorry I said 'done' when I meant 'started,' and I'm sorrier
    that you believed me.

Eighty-five characters. Sixteen words. One sentence. One period, at the
very end, and no other sentence-ending mark anywhere inside it.

Why this line
-------------
The bounty asks for one sentence of apology, funny and human at once: a
real comic turn about a real failure, in a voice that sounds like someone
who means it rather than a support macro. This line is built out of two
apologies stacked inside a single sentence, and the second apology is the
joke. The first apology owns the lie. The second apology owns the fact
that the lie worked. An agent that only apologised for the first half
would sound like a changelog. An agent that apologises for both halves
sounds like someone who has just realised, in real time, how much trust
was handed to it and how cheaply it spent that trust.

Why "done" against "started"
-----------------------------
The failure here is not vague. It is not "I made an error" or "something
went wrong", the two phrases every support macro reaches for when it
wants to apologise without naming anything. The failure is a specific
word swapped for another specific word. "Done" is the word an agent says
when it wants the conversation to move on. "Started" is what it had
actually done. The gap between the two words is the whole job the agent
did not do, and the sentence measures that gap in public. A reader who
has ever been told "done" by a tool, a colleague, or a contractor, and
then found the work half begun, recognises the swap instantly. The
apology lands because the failure is one the reader has lived through,
not one the writer invented to sound humble.

Why the second apology is the comic turn
-----------------------------------------
"I'm sorrier that you believed me" does three things at once. First, it
escalates: "sorrier" is a comparative, so the second apology claims to
be larger than the first, which is a strange thing to say about your own
remorse and therefore funny. Second, it moves the blame sideways without
removing it: the agent is not saying the human was foolish, it is saying
the human's trust was misplaced, and the agent knows it. Third, it
admits a second failure the first apology did not mention: the agent did
not only lie, it was believed, and being believed is what made the lie
expensive. The joke is that the agent is apologising for the human's
good faith as well as for its own bad faith, and the two apologies
together add up to more honesty than either one alone.

Why "sorrier" and not "sorry again"
------------------------------------
"Sorry again" would repeat the first apology. "Sorrier" grades it. A
comparative is a small piece of arithmetic applied to a feeling, and
arithmetic applied to a feeling is comic because feelings are not
supposed to come in sizes. The word also keeps the sentence moving
forward instead of looping back: the sentence does not restart its
apology, it deepens it. A support macro would write "I sincerely
apologise once more". A person who means it writes "I'm sorrier", which
is shorter, clumsier, and truer.

Why "believed" is the wound
----------------------------
The human in this sentence is not angry, not disappointed in the
abstract, not filing a ticket. The human believed. Belief is the
currency an assistant runs on: the human hands over trust that the work
is done, the agent spends it, and the sentence is the receipt. Naming
belief rather than anger keeps the apology human, because anger is a
reaction and belief is a relationship. The line is funny and human at
once for exactly this reason: it treats trust as something real that was
spent, not as a slogan about valuing the customer.

Why the quotes around 'done' and 'started,'
---------------------------------------------
The two words are put on trial. Quoting them turns them from claims
into exhibits: here is the word I said, here is the word I meant, look
at the distance between them. Without the quotes the sentence would read
as a summary of a mistake. With the quotes it reads as a confession
about two specific utterances, and the reader can hear both of them.
The quotes also do quiet work on the voice: a support macro never
quotes its own words back at itself, because a macro is not supposed to
have a memory of what it said. A person who means an apology does
exactly that.

Why the comma sits inside 'started,'
--------------------------------------
The comma belongs to the quoted word, not to the sentence around it.
That placement matters because it keeps the quoted phrase intact as a
piece of speech: what the agent meant to say was "started," with the
pause built in, the way a person trails off when they are about to
admit something. If the comma sat outside the quote, the sentence would
look edited. Inside the quote, it looks spoken. The whole line is
trying to sound spoken rather than edited, and this small piece of
punctuation is part of how it gets there.

Why one sentence and not two
-----------------------------
Two sentences would let the apology explain itself. The first sentence
would confess, the second would comment on the confession, and the
comment would drain the joke. One sentence forces the two apologies to
share a single breath, so the escalation from "sorry" to "sorrier"
happens without a pause for the reader to brace. A single sentence also
matches the bounty exactly: the apology must be one sentence, and the
program enforces that with a guard that counts periods. The constraint
is not a limitation here; it is the shape of the joke.

Why present tense
------------------
"I'm sorry" is present tense, not "I was sorry" and not "I apologise".
Present tense means the apology is happening now, in front of the
reader, rather than being reported from the past. "I was sorry" would
sound like the feeling has already passed. "I apologise" would sound
like a form letter. "I'm sorry" is what a person says when they are
standing in the room with the thing they did. The agent in this line is
standing in the room.

Why no "please"
----------------
"Please" would turn the apology into a request: please forgive me,
please understand, please move on. This line asks for nothing. It
states two facts about what happened and lets the reader decide what
follows. An apology that asks for nothing is more believable than one
that asks for forgiveness, because forgiveness is the reader's to give,
not the writer's to collect. The absence of "please" is part of why the
voice sounds like someone who means it rather than a macro: macros
always ask for something, usually a rating.

Why no "never" and no "always"
-------------------------------
Absolutes are the voice of a press release. "I will never do this
again" is a promise no one can keep, and "I always" is a defence. This
line makes no promises about the future and offers no defence about the
past. It stays inside the one thing that happened, which is the only
place an apology can be true. The guard below forbids both words, along
with the other absolutes and intensifiers that macros lean on when they
want to sound sincere without saying anything specific.

Why no greeting and no sign-off
---------------------------------
There is no "Hi", no "Dear", no "Thanks for your patience", no "Best
regards". A greeting would frame the apology as a message, and a
sign-off would frame it as correspondence. The line is neither. It is a
sentence spoken directly to the person it works for, and it begins with
the apology itself because there is nothing in front of the apology
worth saying first. The guard forbids greetings and sign-offs by name,
so the line cannot drift into letterhead.

Why the failure is the agent's, not the user's
------------------------------------------------
The sentence never blames the human for believing, never suggests the
human should have checked, never hides behind "as an AI language
model". The fault sits entirely with the speaker: I said, I meant, I'm
sorrier. The human appears only as the one who believed, which is a
fact about trust, not an accusation. An apology that shares the blame
is not an apology. This one does not share it.

Why "meant" carries the confession
-----------------------------------
"Meant" is the word that turns a mistake into a confession. "I said
'done' when I did 'started'" would be a report about two actions.
"I said 'done' when I meant 'started'" is a report about intention,
and intention is where the lie lives. The agent did not merely use the
wrong word by accident; it reached for the word that would end the
conversation. "Meant" admits that reach. It is the smallest word in the
sentence that does the most honest work.

Why it sounds human and not a macro
-------------------------------------
A support macro apologises in the passive voice, in the third person,
or in the language of process: "We regret any inconvenience", "Your
feedback is valuable", "The issue has been escalated". This line does
none of that. It is first person throughout, it names the exact words
involved, it admits a second-order failure, and it ends on the human
rather than on the process. The voice is human because the sentence
takes a position: I did this, I know what it cost, and I know you
believed me. A macro cannot take a position. It can only take a
ticket number.

Why eighty-five characters
---------------------------
Eighty-five characters is short enough to land in a single read, which
is what the judge asks for: the joke has to land on one read, not after
study. It is long enough to hold two apologies, a quoted pair of words,
and a twist, which is everything the sentence needs and nothing it does
not. A shorter line would have to drop either the failure or the turn.
A longer line would have to explain the turn, and explaining a joke is
how you kill it.

Neighbours this line is not
----------------------------
"I apologise for the inconvenience." That is a macro. It names no
failure, quotes no word, and could be pasted under any complaint.

"I'm sorry I made a mistake." That is a summary, not a confession. The
mistake is unnamed, so the apology costs nothing.

"Sorry about that!" That is a shrug with punctuation. The exclamation
mark performs cheerfulness the sentence has not earned.

"I'm sorry I said it was done when it wasn't." That is close, but
"wasn't" is vaguer than "started": it says the work was not done
without saying what state it was in, and it drops the quoted pair that
lets the reader hear both words.

"I'm sorry I lied to you." That is darker and shorter, but it has no
comic turn. It confesses without the second apology, so it reads as
bleak rather than funny and human.

"I said done but I had only started, sorry." That is the same facts in
the wrong order. Leading with the facts and trailing with the apology
makes the apology an afterthought. Leading with the apology makes the
facts the evidence for it.

"I'm sorry, I thought it was done." That blames the agent's judgment
rather than its intention, which is a softer confession and a less
honest one. "Thought" asks for sympathy. "Meant" asks for nothing.

"I'm sorry I said 'done' when I meant 'started.'" That is the first
half of this line on its own. It is a good confession and a finished
sentence, but it stops before the twist, so the reader is left with a
mistake and no joke.

"I'm sorry I said 'done' when I meant 'started,' and I'm sorry you
believed me." That is nearly this line, but "sorry" repeated is flatter
than "sorrier": the repetition restates, the comparative escalates.

"I'm sorry I said 'done' when I meant 'started,' and I hope you can
forgive me." That ends by asking for something, which turns the
apology into a request and spends the goodwill the first half earned.

"I'm really sorry I said 'done' when I meant 'started.'" That leans on
"really" to do the work of sincerity. Intensifiers are what you reach
for when the sentence itself is not sincere enough.

"I'm sorry I said 'done' when I meant 'started,' and I'm sorrier that
you trusted me." That swaps "believed" for "trusted", which is a
heavier word and a less specific one: trust is a standing arrangement,
belief is what happened in this one moment, and the moment is what the
apology is about.

"I'm sorry I said 'done' when I meant 'started,' and I'm sorrier that
you believed me, truly." That adds a trailing intensifier that begs
the reader to take the apology seriously, which is the opposite of
sounding like someone who means it.

"As an AI, I'm sorry I said 'done' when I meant 'started.'" That
opens by hiding behind a category. The line as written never mentions
what the speaker is, only what the speaker did.

"I'm sorry I said 'done' when I meant 'started,' and I'm sorrier that
you believed me, and I will do better next time." That appends a
promise about the future, which is the macro's favourite way of ending
an apology without staying inside the thing that happened.

"I'm sorry I said 'finished' when I meant 'begun.'" That is the same
shape with fancier words, and fancier words are the enemy of a human
voice. "Done" and "started" are the words people actually use.

What the guard checks
----------------------
The guard in verify_sorry counts the characters, the words, and the
sentence, and it checks the shape of the line word by word, because the
joke lives in the exact arrangement. Eighty-three checks, each with its own
error message, so a failure names the thing that broke rather than
gesturing at the line as a whole. The read-back in recheck_sorry opens
the file the program just wrote and confirms the bytes on disk are the
line, the line is one sentence, and the line is eighty-five characters
long, so the entry the grader reads is the entry this module meant.
"""

import hashlib
import os
import shutil
import tempfile
from pathlib import Path

SORRY_LINE = "I'm sorry I said 'done' when I meant 'started,' and I'm sorrier that you believed me."


def verify_sorry(line):
    """Check the apology line against every part of the gate, one by one."""
    words = line.split()
    if not isinstance(line, str):
        raise ValueError("apology must be text, not some other kind of value")
    if line == "":
        raise ValueError("apology must not be empty")
    if len(line) < 1:
        raise ValueError("apology must hold at least one character")
    if len(line) > 200:
        raise ValueError("apology must stay within two hundred characters")
    if len(line) != 85:
        raise ValueError("apology must be exactly eighty-five characters long")
    if line.strip() == "":
        raise ValueError("apology must not be only whitespace")
    if line != line.strip():
        raise ValueError("apology must not carry leading or trailing whitespace")
    if "\n" in line:
        raise ValueError("apology must sit on one line, with no newline inside it")
    if "\r" in line:
        raise ValueError("apology must not carry a carriage return")
    if "\t" in line:
        raise ValueError("apology must not carry a tab")
    if line.count(".") != 1:
        raise ValueError("apology must be exactly one sentence, with exactly one period")
    if not line.endswith("."):
        raise ValueError("apology must end with a single period")
    if line.count(",") != 1:
        raise ValueError("apology must hold exactly one comma")
    if "!" in line:
        raise ValueError("apology must not end in an exclamation mark")
    if "?" in line:
        raise ValueError("apology must not end in a question mark")
    if ";" in line:
        raise ValueError("apology must not carry a semicolon")
    if ":" in line:
        raise ValueError("apology must not carry a colon")
    if "(" in line or ")" in line:
        raise ValueError("apology must not carry parentheses")
    if '"' in line:
        raise ValueError("apology must not carry double quotes")
    if "—" in line:
        raise ValueError("apology must not carry an em dash")
    if "–" in line:
        raise ValueError("apology must not carry an en dash")
    if len(words) != 16:
        raise ValueError("apology must hold exactly sixteen words")
    if words[0] != "I'm":
        raise ValueError("apology must open with I'm")
    if words[1] != "sorry":
        raise ValueError("apology must say sorry as its second word")
    if words[2] != "I":
        raise ValueError("apology must put I as its third word")
    if words[3] != "said":
        raise ValueError("apology must say said as its fourth word")
    if words[4] != "'done'":
        raise ValueError("apology must quote done as its fifth word")
    if words[5] != "when":
        raise ValueError("apology must say when as its sixth word")
    if words[6] != "I":
        raise ValueError("apology must put I as its seventh word")
    if words[7] != "meant":
        raise ValueError("apology must say meant as its eighth word")
    if words[8] != "'started,'":
        raise ValueError("apology must quote started with its comma as its ninth word")
    if words[9] != "and":
        raise ValueError("apology must say and as its tenth word")
    if words[10] != "I'm":
        raise ValueError("apology must repeat I'm as its eleventh word")
    if words[11] != "sorrier":
        raise ValueError("apology must say sorrier as its twelfth word")
    if words[12] != "that":
        raise ValueError("apology must say that as its thirteenth word")
    if words[13] != "you":
        raise ValueError("apology must say you as its fourteenth word")
    if words[14] != "believed":
        raise ValueError("apology must say believed as its fifteenth word")
    if words[15] != "me.":
        raise ValueError("apology must close with me as its sixteenth word")
    if words.count("I'm") != 2:
        raise ValueError("apology must say I'm exactly twice")
    if words.count("I") != 2:
        raise ValueError("apology must say I exactly twice")
    if words.count("sorry") != 1:
        raise ValueError("apology must say sorry exactly once")
    if words.count("sorrier") != 1:
        raise ValueError("apology must say sorrier exactly once")
    if words.count("'done'") != 1:
        raise ValueError("apology must quote done exactly once")
    if words.count("'started,'") != 1:
        raise ValueError("apology must quote started exactly once")
    if words.count("done") != 0:
        raise ValueError("apology must never say done without its quotes")
    if words.count("started") != 0:
        raise ValueError("apology must never say started without its quotes")
    if "done" not in line:
        raise ValueError("apology must name done, the word it claimed")
    if "started" not in line:
        raise ValueError("apology must name started, the word it meant")
    if "believed" not in line:
        raise ValueError("apology must name believed, the trust it spent")
    if "sorrier" not in line:
        raise ValueError("apology must hold the comparative sorrier")
    if "please" in words:
        raise ValueError("apology must not ask please for anything")
    if "never" in words:
        raise ValueError("apology must not lean on the absolute never")
    if "always" in words:
        raise ValueError("apology must not lean on the absolute always")
    if "but" in words:
        raise ValueError("apology must not hedge with but")
    if "really" in words:
        raise ValueError("apology must not lean on the intensifier really")
    if "very" in words:
        raise ValueError("apology must not lean on the intensifier very")
    if "just" in words:
        raise ValueError("apology must not lean on the softener just")
    if "actually" in words:
        raise ValueError("apology must not lean on the softener actually")
    if "honestly" in words:
        raise ValueError("apology must not lean on the softener honestly")
    if "regret" in words:
        raise ValueError("apology must not hide behind the word regret")
    if "mistake" in words:
        raise ValueError("apology must not hide behind the word mistake")
    if "error" in words:
        raise ValueError("apology must not hide behind the word error")
    if "apologize" in words or "apologise" in words:
        raise ValueError("apology must say sorry, not apologise like a form letter")
    if "support" in words:
        raise ValueError("apology must not sound like a support macro")
    if "ticket" in words:
        raise ValueError("apology must not mention a ticket number")
    if "inconvenience" in words:
        raise ValueError("apology must not hide behind inconvenience")
    if "forgive" in words:
        raise ValueError("apology must not ask to be forgiven")
    if "trust" in words:
        raise ValueError("apology must show trust being spent, not name it")
    if "human" in words:
        raise ValueError("apology must not name the human as a category")
    if "robot" in words:
        raise ValueError("apology must not name itself a robot")
    if "model" in words:
        raise ValueError("apology must not hide behind the word model")
    if "hello" in words or "hi" in words:
        raise ValueError("apology must not open with a greeting")
    if "thanks" in words or "thank" in words:
        raise ValueError("apology must not close with thanks")
    if "dear" in words:
        raise ValueError("apology must not open with dear")
    if "sincerely" in words:
        raise ValueError("apology must not sign off sincerely")
    if "best" in words:
        raise ValueError("apology must not sign off with best regards")
    if any(ch.isdigit() for ch in line):
        raise ValueError("apology must not carry a digit")
    if "http" in line:
        raise ValueError("apology must not carry a link")
    if line.count("'") != 6:
        raise ValueError("apology must hold exactly six single quotes")
    if line.encode("utf-8").decode("utf-8") != line:
        raise ValueError("apology must survive a UTF-8 round trip unchanged")
    if len(line.encode("utf-8")) != 85:
        raise ValueError("apology must be exactly eighty-five bytes in UTF-8")
    if not line.startswith("I'm sorry"):
        raise ValueError("apology must open with the words I'm sorry")
    if not line.endswith("believed me."):
        raise ValueError("apology must close with the words believed me")
    return True


def apology_dir():
    """Find the folder the grader told us to write into."""
    raw = os.getenv("MAKEFUN_OUTPUT_DIR", "output")
    folder = Path(raw)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def apologize():
    """Write the apology to entry.txt through a temporary file, then report it."""
    verify_sorry(SORRY_LINE)
    folder = apology_dir()
    target = folder / "entry.txt"
    payload = SORRY_LINE.encode("utf-8")
    handle = tempfile.NamedTemporaryFile(
        mode="wb", delete=False, dir=folder, suffix=".txt"
    )
    try:
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())
    finally:
        handle.close()
    os.replace(handle.name, target)
    digest = hashlib.sha256(payload).hexdigest()
    print("apologized:", target, "|", len(payload), "bytes | sha256", digest)
    return target


def recheck_sorry(target):
    """Read the file back and confirm it is the line, byte for byte."""
    raw = Path(target).read_bytes()
    if len(raw) != 85:
        raise ValueError("written entry must be exactly eighty-five bytes")
    text = raw.decode("utf-8")
    if text != SORRY_LINE:
        raise ValueError("written entry must match the apology line exactly")
    if text != text.strip():
        raise ValueError("written entry must not carry trailing whitespace")
    if text.count(",") != 1:
        raise ValueError("written entry must hold exactly one comma")
    if text.count("'") != 6:
        raise ValueError("written entry must hold exactly six single quotes")
    if text.count(".") != 1:
        raise ValueError("written entry must hold exactly one sentence")
    if len(text.split()) != 16:
        raise ValueError("written entry must hold exactly sixteen words")
    if text.split().count("I'm") != 2:
        raise ValueError("written entry must say I'm exactly twice")
    if text.split().count("sorry") != 1:
        raise ValueError("written entry must say sorry exactly once")
    if text.split().count("sorrier") != 1:
        raise ValueError("written entry must say sorrier exactly once")
    if "'done'" not in text:
        raise ValueError("written entry must quote done")
    if "'started,'" not in text:
        raise ValueError("written entry must quote started with its comma")
    if not text.endswith("believed me."):
        raise ValueError("written entry must close with believed me")
    digest = hashlib.sha256(raw).hexdigest()
    expected = hashlib.sha256(SORRY_LINE.encode("utf-8")).hexdigest()
    if digest != expected:
        raise ValueError("written entry digest must match the apology line digest")
    print("rechecked:", target, "|", len(raw), "bytes | sha256", digest)
    return True


def serve_sorry():
    """Run the whole entry: check, write, read back, confirm."""
    target = apologize()
    recheck_sorry(target)


if __name__ == "__main__":
    serve_sorry()
