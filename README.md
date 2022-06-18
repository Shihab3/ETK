# ETK
Easy TKinter library

it is for making tkinter much more easier and less code lines.
Don't forget to click on `Wiki` page.

## Examples:

1. Create cool button in class EButton
```py
ETK.EButton(root, text = "Click Me", 
            styleCode  = "border-thick:4px, font-family:arial, font-size:30px",
            toolTip    = ETK.ETip(text = "This is tooltip for the button", followMouse = True),
            placeMent  = EPlace(x=10, y=10, relwidth=1.0, relx=0.9))
```

2. Create cool path entry so there is everything already managed like the filename and the browse button:
```py
ETK.EPathInput(root, text   = "Open a file",
               styleCode    = "bg: #303030, border-thick: 4px",
               justify      = "left",
               openWinTitle = "insert the path: ",
               buttonStyle  = "bg: #242424, border-thick: 1px, border-color: grey",
               labelStyle   = "bg: #242424, fg: dark orange",
               placeMent    = ETK.EPlace(10, 10))
```

Well... there is more classes but you should try to explore them by yourself.

There is EStaticText, EOptionSelector, EColorPick, ESquare and ETreeView.

## How to use

first you should install these packages `tkinter-tooltip`, `pygame` and `ttkwidgets`.

https://pypi.org/project/tkinter-tooltip/ 

https://pypi.org/project/pygame/ 

https://pypi.org/project/ttkwidgets

in one line: 

`pip install pygame ttkwidgets tkinter-tooltip`

then copy that `ETK` folder into your project and use it.

```py
import ETK
ETK.Exyz
```
