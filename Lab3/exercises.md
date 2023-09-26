# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- I think it is a concrete class, it just has no specific methods and attributes.
2. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- This method is used to destroy the instance we created.
3. What class does Texture inherit from?
	- Texture inherits from Image.
4. What methods and attributes does the Texture class inherit from 'Image'? 
	- Methods: constructor, getWidth(), getHeight(), getPixelColorR(), getPixels(), setPixelsToRandomValue()
	- Attributes:  m_width, m_height, m_colorChannels, m_Pixels
5. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- I think a texture should have a 'has-a' relationship with 'Image'. That is, every images have their own texture. I will add a texture attribute to Image.
6. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- Python do provide a default constructor.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

   It depends on how we implement the singleton pattern. But the default way isn't thread safe. If multiple threads try to create an instance of singleton simultaneously, it's possible that they could end up creating multiple instances.

*edit the code directly*  
  
