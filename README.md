# Primitive ASCII Art Generator
 Generates "primitive" ASCII art. In this case "primitive" means value-based per pixel rather than line- or shape-based.
 
 ---
 ## Statement of Intent
 The idea behind the program is to have a class (`Picture`) that handles all the logic that one could need to handle converting any given picture into both or either a string that can be copied onto the clipboard and/or a .png to share with family, friends or the internet.
 
 My goals for this project are:
 
 - [x] Easy to use
 - [x] Minimal boilerplate for end user (might be the same thing as "easy to use")
 - [ ] Makes reasonably-sized .pngs
 - [x] and, most importantly, done.
 
---
## Examples
Due to the nature of using one ASCII character per pixel in the finished image the final product's dimensions are expanded by a factor of the horizontal size of the character in pixels. For instance, in this case the font is 20 pt. Courier which has a width of twelve pixels making the final product twelve times wider than the original image. This may or may not be fixed in an update.

### Original
![A picture I took of a nickel from 1941](Examples/example_nickel.png)

### ASCII approximation
![The same picture made up of ASCII characters](Examples/example_nickel_ascii.png)

### Colored ASCII (beta)
![The same picture made up of the same ASCII Characters but this time with the color of the original image overlaid on the text](Examples/example_nickel_ascii_color.png)

### Raw ASCII string
See the file [example_ascii_nickel.txt](Examples/example_ascii_nickel.txt) (for this example the original picture has been resized to be two hundred pixels wide)
