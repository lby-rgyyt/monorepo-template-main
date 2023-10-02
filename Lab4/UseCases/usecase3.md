**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 3

<hr>

**Use Case**: Clear canvas

**Primary Actor**: User

**Goal in Context**: To clear the entire canvas

**Preconditions**: There must be an existing canvas and in a responsive state

**Trigger**: Press the space
  
**Scenario**: A user will press the space when they want to clear the whole canvas to restart painting.
 
**Exceptions**: The program may become potentially unresponsive. In this case, the program can be terminated from the operating system.

**Priority**: High-priority

**When available**: First release

**Channel to actor**: The primary actor communicates through I/O devices. This includes the keyboard. The system is responsible for maintaining focus of the window when the user presses keyboard, and should respond within 1 second of pressing space event. The user is responsible for all other input.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: We might need to double check with users before the program really clears the canvas.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
