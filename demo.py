import ETK
import tkinter as tk

root = tk.Tk(); root.geometry('800x800'); root.title('Demo ETK'); root['bg'] = "#242424"

Button        = ETK.EButton(root, text="EButton",image="demoFiles\\the-promised-neverland-smile.gif",
                            placeMent=ETK.EPlace(10, 80), toolTip=ETK.ETip('This is ToolTip'))

Text          = ETK.EStaticText(root,"EStaticText",img=ETK.EImage("demoFiles\\Loading.gif","X:64,Y:64"),
                                placeMent=ETK.EPlace(10,420),styleCode='bg:#242424,fg:white')

PathEntry     = ETK.EPathInput     (root,placeMent=ETK.EPlace(10,30),type='FILE')
OptionSelector= ETK.EOptionSelector(root,text='EOptionSelector',placeMent=ETK.EPlace(100,470))
colorChooser  = ETK.EColorPick     (root,text='EColorPick',styleCode='font-size:10px,border-thick:0px',placeMent=ETK.EPlace(x=220,y=430,width=64,height=54))
shape         = ETK.ESquare        (root,text='ESquare',placeMent=ETK.EPlace(10,530,width=64,height=64),textSpace=1)

OptionSelector.addOption('Blah')
print(OptionSelector.getOptions())
OptionSelector.rePaint()

treeView     = ETK.ETreeView(root,placeMent=ETK.EPlace(290,10,width=400))
treeView.setColumns(('Name','Data'))
treeView.addItem('0.',{'Name':'ETK','Data':'v0.05ACC'})
treeView.addParentItem('0.0.','0.',{'Name':'EI','Data':'v0.01'})
treeView.addItem('1.',{'Name':'ATK','Data':'v0.01 Alpha'})
treeView.addItem('2.',{'Name':'ITK','Data':'v0.01 Alpha'})
treeView.addItem('3.',{'Name':'VTK','Data':'v0.01 Alpha'})
treeView.addItem('4.',{'Name':'GTKN','Data':'v0.01 Alpha'})

treeView.chessTheme()
root.mainloop()
