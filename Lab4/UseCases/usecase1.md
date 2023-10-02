**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 1

<hr>

**Use Case**: Create canvas

**Primary Actor**: User

**Goal in Context**: To create a drawable canvas

**Preconditions**: There must be enough blank space to create a new window.

**Trigger**: (1) Click 'create' button. (2) Short key.
  
**Scenario 1**: The user will click the 'create' button located in the bottom-right corner to create a new canvas.

**Scenario 2**: The user will press short key like 'cmd+N' to create a new canvas.
 
**Exceptions**: If there is no enough space, the program will not create a new canvas sucessfully.

**Priority**: High-priority

**When available**: First release

**Channel to actor**: The primary actor communicates through I/O devices. This includes the keyboard and the mouse. The system is responsible for maintaining focus of the window when the user clicks, and should respond within 1 second of any keyboard event. The user is responsible for all other input.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: Before create a new canvas, we might need to detect whether there is enough space and warn users in advance.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
