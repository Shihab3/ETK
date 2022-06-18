import os, shutil
from PIL import Image, ImageTk, ImageFilter
from pygame import mixer
import tkinter as tk
from tktooltip import ToolTip as TT
from tkinter import filedialog, ttk
from ttkwidgets.color import askcolor
from pydoc import importfile

mixer.init()
defaultStyle = {'bg'            :'#242424',
                'fg'            :"white",
                'border-color'  :"grey",
                'border-thick'  :3,
                'active-bg'     :'orange',
                'active-fg'     :'white',
                'compund-image' :'top',
                'menu-bg'       :'#303030',
                'menu-fg'       :'white',
                'menu-active-bg':'orange',
                'menu-active-fg':'white',
                'arrow-color'   :'white',
                'font-family'   :'Bauhaus 93',
                'font-size'     :10,
                'font-type'     :'normal'
                }

longExtensions = (('Images Files'    , '*.png *.jpg *.gif *.jpeg *.bmp *.tif *.tiff'), 
                  ('Sound Files'     , '*.mp3 *.ogg *.wav *.cda *.m4a'),
                  ('Video Files'     , '*.mp4 *.mov *.avi *.flv *.vob *.wmv'),
                  ('CenoEngine Files', '*.ceno *.pack'),
                  ('Python Files'    , '*.py'),
                  ('C++ Files'       , '*.cpp *.cxx *.chh *.H'),
                  ('C Files'         , '*.c *.h'),
                  ('Text Files'      , '*.txt *.rtf'),
                  ('Binary Files'    , '*.bin *.obj *.o'),
                  ('HTML Files'      , '*.html *.htm *.css *.js'),
                  ('PDF Files'       , '*.pdf'),
                  ('System Files'    , '*.exe *.bat *.dll *.ini *.msi *.sys *.tmp'),
                  ('Compressed Files', '*.zip *.rar *.cap *.iso'),
                  ('Java Files'      , '*.java *.jar'),
                  ('PowerPoint Files', '*.pot *.potm *.potx *.ppam *.pps *.ppsm *.ppsx *.ppt *.pptm *.pptx'),
                  ('AdobePhotoshop'  , '*.psd'),
                  ('All Files'       , '*.*')
                  )

def __compileStyle__(code:str):
    code       = code.replace('px', '')
    code       = code.replace(" ", "")
    Values     = code.split  (',')
    bg         = defaultStyle["bg"]
    fg         = defaultStyle["fg"]
    bordercolor= defaultStyle["border-color"]
    borderThick= defaultStyle["border-thick"]
    activebg   = defaultStyle["active-bg"]
    activefg   = defaultStyle["active-fg"]
    compundimg = defaultStyle["compund-image"]
    menubg     = defaultStyle["menu-bg"]
    menufg     = defaultStyle["menu-fg"]
    amenubg    = defaultStyle["menu-active-bg"]
    amenufg    = defaultStyle["menu-active-fg"]
    arrowcolor = defaultStyle["arrow-color"]
    fontFamily = defaultStyle["font-family"]
    fontSize   = defaultStyle["font-size"]
    fontType   = defaultStyle["font-type"]

    for i in range(len(Values)):
        AfterSplit = Values[i].split(':')
        if AfterSplit[0] == 'bg'            : bg          =AfterSplit[1]
        if AfterSplit[0] == 'fg'            : fg          =AfterSplit[1]
        if AfterSplit[0] == 'border-color'  : bordercolor =AfterSplit[1]
        if AfterSplit[0] == 'border-thick'  : borderThick =int(AfterSplit[1])
        if AfterSplit[0] == 'active-bg'     : activebg    =AfterSplit[1]
        if AfterSplit[0] == 'active-fg'     : activefg    =AfterSplit[1]
        if AfterSplit[0] == 'compund-img'   : compundimg  =AfterSplit[1]
        if AfterSplit[0] == 'menu-bg'       : menubg      =AfterSplit[1]
        if AfterSplit[0] == 'menu-fg'       : menufg      =AfterSplit[1]
        if AfterSplit[0] == 'menu-active-bg': amenubg     =AfterSplit[1]
        if AfterSplit[0] == 'menu-active-fg': amenufg     =AfterSplit[1]
        if AfterSplit[0] == 'arrow-color'   : arrowcolor  =AfterSplit[1]
        if AfterSplit[0] == 'font-family'   : fontFamily  =AfterSplit[1]
        if AfterSplit[0] == 'font-size'     : fontSize    =int(AfterSplit[1])
        if AfterSplit[0] == 'font-type'     : fontType    =AfterSplit[1]
    
    finishValue = {'bg'             : bg         , 
                   'fg'             : fg         ,
                   'border-color'   : bordercolor, 
                   'border-thick'   : borderThick,
                   'active-bg'      : activebg   , 
                   'active-fg'      : activefg   , 
                   'compund-image'  : compundimg , 
                   'arrow-color'    : arrowcolor ,
                   'menu-bg'        : menubg     , 
                   'menu-fg'        : menufg     , 
                   'menu-active-bg' : amenubg    , 
                   'menu-active-fg' : amenufg    ,
                   'font'           : EFont(fontFamily,fontSize,fontType)
                   }
    return finishValue

def __convertAny__(code:str):
    code = code.replace('px', '')
    code = code.replace(" ", "")
    Values = code.split(',')
    Finish = {}

    for i in range(len(Values)):
        try:
            AfterSplit = Values[i].split(':')
            Finish[AfterSplit[0]]=AfterSplit[1]
        except:
            print('WARNING: There is an error in convertAny func')
    
    return Finish

def __convertImg__(code:str):
    filter_types = 'BLUR CONTOUR DETAIL SHARPEN SMOOTH'.split(' ')
    code = code.replace('px', '')
    code = code.replace(" ", "")
    Values = code.split(',')
    filer=None; x=None; y=None; 
    for i in range(len(Values)):
        AfterSplit = Values[i].split(':')
        if AfterSplit[0] == 'filter' : 
            for i in range(len(filter_types)):
                if AfterSplit[1] == filter_types[i]:
                    filer=AfterSplit[1]
        if AfterSplit[0] == 'X'      : x=AfterSplit[1]
        if AfterSplit[0] == 'Y'      : y=AfterSplit[1]

    FinishValue={'filter':filer, 'X':x, 'Y':y}
    return FinishValue

#### Elements ####

class EFont:
    def __init__(self, 
                 fontFamily=defaultStyle['font-family'], 
                 fontSize=defaultStyle['font-size'], 
                 fontType=defaultStyle['font-type']):
        self.family = fontFamily
        self.size   = fontSize
        self.type   = fontType

    def get(self, type=tuple):
        if type == tuple:
            return (self.font, self.fontsize, self.fonttype)
        elif type == list:
            return [self.font, self.fontsize, self.fonttype]
        elif type == dict:
            return {'font': self.font, 'fontsize': self.fontsize, 'fonttype': self.fonttype}

class ETip:
    def __init__(self, text, delay=0.1, x=25, y=25, bg="#454545",fg="white",followMouse=True,toolTipSwitch=True) -> None:
        """
            ETip is a class that contine values of toolTip placment.
        """
        self.text=text; self.delay=delay; self.x=x; self.y=y; self.bg=bg; self.fg=fg; self.follwMouse=followMouse
        self.toolTipSwitch = toolTipSwitch

    def get(self, type=dict):
        if type == tuple:
            return (self.text, self.delay, self.x, self.y)
        elif type == list:
            return [self.text, self.delay, self.x, self.y]
        elif type == dict:
            return {'text': self.text, 'delay': self.delay, 'x': self.x, 'y': self.y, 'fg': self.fg, 'bg': self.bg}

class EPlace:
    def __init__(self, x, y, relwidth=None, relheight=None, relx=None, rely=None, width=None, height=None) -> None:
        """
            EPlace is a class that have the place placestem elements could be used in Widget Classes.
        """
        self.x = x; self.y = y; self.relwidth = relwidth; self.relheight = relheight; self.relx = relx; self.rely = rely
        self.width = width; self.height = height
    
    def Set(self, x, y, relwidth=None, relheight=None, relx=None, rely=None, width=None, height=None):
        """
            set class values if you want to.
        """
        self.x = x; self.y = y; self.relwidth = relwidth; self.relheight = relheight; self.relx = relx; self.rely = rely
        self.width = width; self.height = height
    def get(self, type=dict):
        """
            get class values if you want to.
        """
        if type == tuple:
            return (self.x, self.y, self.relwidth, self.relheight, self.relx, self.rely, self.width, self.height)
        elif type == list:
            return [self.x, self.y, self.relwidth, self.relheight, self.relx, self.rely, self.width, self.height]
        elif type == dict:
            return {'x': self.x, 'y': self.y, 'relwidth': self.relwidth, 'relheight': self.relheight, 'relx': self.relx, 'rely': self.rely, 
                    'width' : self.width, 'height' : self.height}

class EPath:
    def __init__(self) -> None: 
        """
            Playing with path placestem.
            Remove, Add, Backword, ... paths.
        """
        pass
    def Backward(Path:str):
        """
            if you have path like c:/user/blah, and you called this method on it.
            will be c:/user which mean backward a step in a path.
        """
        return os.path.dirname(Path)
    def removeContentsFolder(folder:str):
        """
            Remove any files in the specific folder.
        """
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

class EImage(ImageTk.PhotoImage):
    def __init__(self,img:str, ImgStyle=None):
        if os.path.exists(img):
            self.imgpath = img
            self.load = Image.open(img)
        else:
            if os.path.exists(os.path.join(Folder, img)):
                self.imgpath = os.path.join(Folder, img)
                self.load = Image.open(self.imgpath)
            else:
                if os.path.exists(os.path.join(FolderETK, img)):
                    self.imgpath = os.path.join(FolderETK, img)
                    self.load = Image.open(self.imgpath)
                else:
                    raise Exception("Path Invalid","No such file or directory: "+img)
        if ImgStyle != None:
            ImageStyle = __convertImg__(ImgStyle)
            gg = self.imgpath.split('\\')
            if ImageStyle['filter'] == 'BLUR'   : load = load.filter(ImageFilter.BLUR   ); load.save(f'c:\\Windows\Temp\\{gg[-1]}'); self.imgpath = f'c:\\Windows\Temp\\{gg[-1]}'
            if ImageStyle['filter'] == 'CONTOUR': load = load.filter(ImageFilter.CONTOUR); load.save(f'c:\\Windows\Temp\\{gg[-1]}'); self.imgpath = f'c:\\Windows\Temp\\{gg[-1]}'
            if ImageStyle['filter'] == 'DETAIL' : load = load.filter(ImageFilter.DETAIL ); load.save(f'c:\\Windows\Temp\\{gg[-1]}'); self.imgpath = f'c:\\Windows\Temp\\{gg[-1]}'
            if ImageStyle['filter'] == 'SHARPEN': load = load.filter(ImageFilter.SHARPEN); load.save(f'c:\\Windows\Temp\\{gg[-1]}'); self.imgpath = f'c:\\Windows\Temp\\{gg[-1]}'
            if ImageStyle['filter'] == 'SMOOTH' : load = load.filter(ImageFilter.SMOOTH ); load.save(f'c:\\Windows\Temp\\{gg[-1]}'); self.imgpath = f'c:\\Windows\Temp\\{gg[-1]}'
            else: pass
            self.load = Image.open(self.imgpath)
            x_1 = int(ImageStyle['X']); y_1 = int(ImageStyle['Y'])
            self.imgpath = os.path.join(Folder, img)
            ff = self.load.n_frames

            if ff >= 3 and self.imgpath.split('.')[-1] == 'gif':
                if os.path.exists(f'c:\\Windows\Temp\\{gg[-1]}'):
                    os.remove(f'c:\\Windows\Temp\\{gg[-1]}')
                os.system(f'ffmpeg -hide_banner -v warning -i {self.imgpath} -filter_complex "[0:v] scale={x_1}:-1:flags=lanczos,split [a][b]; [a] palettegen=reserve_transparent=on:transparency_color=ffffff [p]; [b][p] paletteuse" '+f'"c:\\Windows\Temp\\{gg[-1]}"')
                self.imgpath = f'c:\\Windows\Temp\\{gg[-1]}'
                self.load = Image.open(self.imgpath)  
            else:
                if x_1 != None and y_1 != None:
                    self.size = (int(x_1), int(y_1))
                    self.load = self.load.resize(self.size, Image.ANTIALIAS)
            
        super().__init__(self.load)
        self.img = ImageTk.PhotoImage(self.load)

class EStyle(object):
    def __init__(self, 
                 styleCode=''):
        self.styleCode     = styleCode
        self.style         = __compileStyle__(self.styleCode)
        self.bg            = self.style["bg"]
        self.fg            = self.style["fg"]
        #self.bd            = self.style["bd"]
        self.border_color  = self.style["border-color"]
        self.border_thick  = self.style["border-thick"]
        self.active_bg     = self.style["active-bg"]
        self.active_fg     = self.style["active-fg"]
        self.compund_image = self.style["compund-image"]
        self.menu_bg       = self.style["menu-bg"]
        self.menu_fg       = self.style["menu-fg"]
        self.menu_active_bg= self.style["menu-active-bg"]
        self.menu_active_fg= self.style["menu-active-fg"]
        self.arrow_color   = self.style["arrow-color"]
        self.font          = self.style["font"]

class EToolTip(TT):
    def __init__(self,
                 widget,
                 text,
                 toolTipSwitch=True,
                 styleCode='',
                 delay=250,
                 followMouse=True):

        self.t = EStyle(styleCode)
        self.text = text
        self.delay = delay
        self.widget = widget
        self.toolTipSwitch = toolTipSwitch
        self.followMouse = followMouse

        ## toolTip ##
        if self.toolTipSwitch == True:
            try:
                if self.widget['state'] == 'disabled':
                    super().__init__(self.widget, 
                                    msg=self.text + ' (Disabled)', 
                                    delay=self.delay,
                                    parent_kwargs={"bg": self.t.bg, "padx": 1, "pady": 1},
                                    fg=self.t.fg, bg=self.t.bg, padx=1, pady=1, follow=self.followMouse)
                else:
                    super().__init__(self.widget, 
                                    msg=self.text, 
                                    delay=self.delay,
                                    parent_kwargs={"bg": self.t.bg, "padx": 1, "pady": 1},
                                    fg=self.t.fg, bg=self.t.bg, padx=1, pady=1, follow=self.followMouse)
            except:
                super().__init__(self.widget, 
                                    msg=self.text, 
                                    delay=self.delay,
                                    parent_kwargs={"bg": self.t.bg, "padx": 1, "pady": 1},
                                    fg=self.t.fg, bg=self.t.bg, padx=1, pady=1, follow=self.followMouse)

    def update(self):
        self.destroy()
        if self.toolTipSwitch == True:
            try:
                if self.widget['state'] == 'disabled':
                    super().__init__(self.widget, 
                                    msg=self.text + ' (Disabled)', 
                                    delay=self.delay,
                                    parent_kwargs={"bg": self.t.bg, "padx": 1, "pady": 1},
                                    fg=self.t.fg, bg=self.t.bg, padx=1, pady=1, follow=self.followMouse)
                else:
                    super().__init__(self.widget, 
                                    msg=self.text, 
                                    delay=self.delay,
                                    parent_kwargs={"bg": self.t.bg, "padx": 1, "pady": 1},
                                    fg=self.t.fg, bg=self.t.bg, padx=1, pady=1, follow=self.followMouse)
            except:
                super().__init__(self.widget, 
                                    msg=self.text, 
                                    delay=self.delay,
                                    parent_kwargs={"bg": self.t.bg, "padx": 1, "pady": 1},
                                    fg=self.t.fg, bg=self.t.bg, padx=1, pady=1, follow=self.followMouse)

Folder    = EPath.Backward (os.path.dirname(os.path.abspath(__file__)))
FolderETK = EPath.Backward (os.path.abspath(__file__))
EI        = importfile(os.path.join(FolderETK,'EI.py'))
#############################################################
def setImageWidget(m,widget,img):
        if img != None and not isinstance(img,str):
            widget.img = img
            try:
                widget.frameCnt = widget.img.load.n_frames
                widget.frames = [tk.PhotoImage(file=widget.img.imgpath,format = 'gif -index %i' %(i)) for i in range(widget.frameCnt)]
                m.after(0, widget.updateImage, 0)
            except:
                widget.configure(image=widget.img)
                widget.image = widget.img
        if isinstance(img,str):
            if os.path.exists(img):
                widget.img = EImage(img)
                try:
                    widget.frameCnt = widget.img.load.n_frames
                    widget.frames = [tk.PhotoImage(file=widget.img.imgpath,format = 'gif -index %i' %(i)) for i in range(widget.frameCnt)]
                    widget.m.after(0, widget.updateImage, 0)
                except:
                    widget.configure(image=widget.img)
                    widget.image = widget.img
            else:
                if os.path.exists(os.path.join(Folder,img)):
                    widget.img = EImage(img)
                    try:
                        widget.frameCnt = widget.img.load.n_frames
                        widget.frames = [tk.PhotoImage(file=widget.img.imgpath,format = 'gif -index %i' %(i)) for i in range(widget.frameCnt)]
                        widget.m.after(0, widget.updateImage, 0)
                    except:
                        widget.configure(image=widget.img)
                        widget.image = widget.img
                else:
                    if os.path.exists(os.path.join(FolderETK,img)):
                        widget.img = EImage(img)
                        try:
                            widget.frameCnt = widget.img.load.n_frames
                            widget.frames = [tk.PhotoImage(file=widget.img.imgpath,format = 'gif -index %i' %(i)) for i in range(widget.frameCnt)]
                            widget.m.after(0, widget.updateImage, 0)
                        except:
                            widget.configure(image=widget.img)
                            widget.image = widget.img
                    else:
                        raise OSError("No such file or directory image at '%s'." % (widget.text))
        else:
            print("No Image will set at '%s'." % (widget.text))

#### Widgets Classes ####

class EButton(tk.Button):
    def __init__(self,
                 master, 
                 text='Button',
                 styleCode='',
                 command=None, 
                 image=None, 
                 placeMent=EPlace(10, 10),
                 toolTip=ETip(text='a button', delay=300)):
        
        self.tip       = toolTip
        self.m         = master 
        self.text      = text
        self.placeMent = placeMent
        self.style     = EStyle(styleCode)
        self.border    = tk.Frame(master,bg=self.style.border_color,bd=0)
        self.frameCnt  = None
        self.frames    = None

        if self.placeMent.width != None and self.placeMent.height != None:
            self.border.config(width = self.placeMent.width +self.style.border_thick*2, 
                               height= self.placeMent.height+self.style.border_thick*2)
        else:
            self.border.config(width = self.style.border_thick*2, 
                               height= self.style.border_thick*2)

        super().__init__(master, 
                         text=text, 
                         command=command, 
                         bd=0, 
                         bg=self.style.bg, 
                         fg=self.style.fg,
                         activebackground=self.style.active_bg, 
                         activeforeground=self.style.active_fg, 
                         font=(self.style.font.family, self.style.font.size, self.style.font.type),
                         compound=self.style.compund_image)

        setImageWidget(self.m,self,image)
        
        self.place(x         = self.placeMent.x       , 
                   y         = self.placeMent.y       , 
                   relx      = self.placeMent.relx    , 
                   rely      = self.placeMent.rely    , 
                   width     = self.placeMent.width   , 
                   height    = self.placeMent.height  , 
                   relwidth  = self.placeMent.relwidth, 
                   relheight = self.placeMent.relheight)
        master.update()
        if self.placeMent.width == None and self.placeMent.height == None:
            self.border.configure(width =self.winfo_width ()+int(self.style.border_thick)*2, 
                                  height=self.winfo_height()+int(self.style.border_thick)*2)

        self.border.place(x=int(self.placeMent.x-int(self.style.border_thick)), 
                          y=int(self.placeMent.y-int(self.style.border_thick)), 
                          relx=self.placeMent.relx, 
                          rely=self.placeMent.rely, 
                          relwidth=self.placeMent.relwidth, 
                          relheight=self.placeMent.relheight)
        

        self.toolTip = EToolTip(self,self.tip.text,delay=self.tip.delay,followMouse=self.tip.follwMouse,toolTipSwitch=self.tip.toolTipSwitch)
    
    def updateImage(self, ind):
        frame = self.frames[ind]
        ind += 1
        if ind == self.frameCnt:
            ind = 0
        self.configure(image=frame)
        self.image = frame
        self.m.after(100, self.updateImage, ind)
    
    def setImage(self,img):
        setImageWidget(self.m,self,img)

class EStaticText(tk.Label):
    def __init__(self, 
                 master, 
                 text='StaticText', 
                 styleCode='',
                 img=None, 
                 placeMent=EPlace(10, 10),
                 toolTip=ETip(text='a text')
                ): 

        ## Vars ##
        self.style     = EStyle(styleCode)
        self.placeMent = placeMent
        self.m         = master
        self.text      = text; 
        self.tip       = toolTip
        
        self.frames    = None
        self.frameCnt  = None

        super().__init__(master, text=text, bd=0, bg=self.style.bg, fg=self.style.fg,
                        activebackground=self.style.active_bg, activeforeground=self.style.active_fg, 
                        font=(self.style.font.family, self.style.font.size, self.style.font.type),
                        compound=self.style.compund_image)
        
        ## Image ##
        setImageWidget(self.m,self,img)
        
        ## Place ##
        self.place(x=placeMent.x, 
                   y=placeMent.y, 
                   relx=placeMent.relx, 
                   rely=placeMent.rely, 
                   width=placeMent.width, 
                   height=placeMent.height)
        self.toolTip   = EToolTip(self,self.tip.text,delay=self.tip.delay,toolTipSwitch=self.tip.toolTipSwitch,followMouse=self.tip.follwMouse)

    def updateImage(self, ind):
        frame = self.frames[ind]
        ind += 1
        if ind == self.frameCnt:
            ind = 0
        self.configure(image=frame)
        self.image = frame
        self.m.after(100, self.updateImage, ind)
    
    def setImage(self,img):
        setImageWidget(self.m,self,img)

class EPathInput(tk.Entry):
    def __init__(self, 
                 master, 
                 text="EPathInput",
                 styleCode='bg:#303030, fg:green, border-thick:2px, border-color:#404040', 
                 placeMent=EPlace(10,10),
                 justify='left', 
                 var=None, 
                 warnColor='yellow', 
                 errorColor='red', 
                 okColor='green', 
                 type='DIR', 
                 openWinTitle='insert the path: ', 
                 extensions=longExtensions, 
                 buttonStyle="bg:#242424,border-thick:1px,border-color:grey",
                 labelStyle="bg:#242424,fg:dark orange"):
        
        self.warnColor    = warnColor
        self.errorColor   = errorColor
        self.okColor      = okColor
        self.type         = type
        self.openWinTitle = openWinTitle
        self.extensions   = extensions
        self.m            = master
        self.buttonStyle  = buttonStyle
        self.labelStyle   = labelStyle
        self.style        = EStyle(styleCode)
        self.placeMent    = placeMent
        self.justify      = justify
        
        if var == None : self.var = tk.StringVar()
        else           : self.var = var
        
        super().__init__(master, bg=self.style.bg, fg=self.style.fg, highlightthickness=self.style.border_thick, 
                         highlightbackground=self.warnColor, highlightcolor=self.warnColor,
                         font=(self.style.font.family, self.style.font.size, self.style.font.type), 
                         justify=justify, textvariable=self.var, bd=0)

        self.place(x=self.placeMent.x, 
                   y=self.placeMent.y, 
                   relheight=self.placeMent.relheight, 
                   relwidth=self.placeMent.relwidth, 
                   relx=self.placeMent.relx, 
                   rely=self.placeMent.rely, 
                   width=self.placeMent.width, 
                   height=self.placeMent.height)
        master.update()
        
        self.buttonWidget = EButton(master, '', image=EImage(os.path.join(FolderETK, 'Data\\FOLDER.png'), 
                                    f'Y:{self.winfo_height()-3}, X:{self.winfo_height()-3}'), 
                                    styleCode=self.buttonStyle, 
                                    placeMent=EPlace(x=self.placeMent.x+self.winfo_width()+1, y=self.placeMent.y), 
                                    command=self.Open, toolTip=ETip('Browse...'))
        
        self.labelWidget  = EStaticText(master, text,styleCode=self.labelStyle,
                                        placeMent=EPlace(x=self.placeMent.x, 
                                        y=self.placeMent.y-self.winfo_height()-1))
        
        master.after(500, self.__rePaint)
        self.var.trace('w', self.__Check)
        self.Tip = TT(self, msg='Insert a path.', parent_kwargs={"bg": "#454545", "padx": 1, "pady": 1},
                      fg="white", bg="#454545", padx=1, pady=1, follow=True)
        self.new_width = self.winfo_width()
        self.old_width = self.winfo_width()
        
    def Open(self):


        if self.type == 'DIR':
            DIR = filedialog.askdirectory(title=self.openWinTitle)
            self.var.set(DIR)
            if os.path.isdir(self.var.get()):
                try:
                    self.Tip.tw.destroy()
                except: pass
                self.config(highlightcolor=self.okColor, highlightbackground=self.okColor, fg=self.okColor)
                self.Tip.msg = 'This path is ok.'
            else:
                try:
                    self.Tip.tw.destroy()
                except: pass
                self.config(highlightcolor=self.errorColor, highlightbackground=self.errorColor, fg=self.errorColor)
                self.Tip.msg = "Can't use this Path !"
        


        elif self.type == 'FILE':
            DIR = filedialog.askopenfilename(title=self.openWinTitle, filetypes=self.extensions)
            self.var.set(DIR)
            if os.path.exists(self.var.get()):
                try:
                    self.Tip.tw.destroy()
                except: pass
                self.config(highlightcolor=self.okColor, highlightbackground=self.okColor, fg=self.okColor)
                self.Tip.msg = 'This path is ok.'
            else:
                try:
                    self.Tip.tw.destroy()
                except: pass
                self.config(highlightcolor=self.errorColor, highlightbackground=self.errorColor, fg=self.errorColor)
                self.Tip.msg = "Can't use this Path !"
      
    def get(self):
        return self.var.get()
    
    def __rePaint(self):
        self.m.update()
        self.new_width = self.winfo_width()
        if self.old_width != self.new_width:
            self.buttonWidget.destroy()
            self.buttonWidget = EButton(self.master, '', image=EImage(os.path.join(FolderETK, 'Data\\FOLDER.png'), 
                                f'Y:{self.winfo_height()-3}, X:{self.winfo_height()-3}'), 
                                styleCode=self.buttonStyle, command=self.Open, toolTip=ETip('Browse...'),
                                placeMent=EPlace(x=self.placeMent.x+self.winfo_width()+1, y=self.placeMent.y))
        else:
            pass
        self.update_idletasks()
        self.old_width = self.winfo_width()
    
    def __Check(self, e, g, h):
        if self.var.get() != '':
            if os.path.isdir(self.var.get()) or os.path.exists(self.var.get()):
                try:
                    self.Tip.tw.destroy()
                except: pass
                self.Tip.msg = 'This path is ok.'
                self.config(highlightcolor=self.okColor, highlightbackground=self.okColor, fg=self.okColor)
            else:
                try:
                    self.Tip.tw.destroy()
                except: pass
                self.config(highlightcolor=self.errorColor, highlightbackground=self.errorColor, fg=self.errorColor)
                self.Tip.msg = "Cannot use this path."
        else:
            try:
                self.Tip.tw.destroy()
            except: pass
            self.config(highlightcolor=self.warnColor, highlightbackground=self.warnColor, fg=self.warnColor)
            self.Tip.msg = "Insert a path."

class EOptionSelector(ttk.OptionMenu):
    def __init__(self, 
                 master, 
                 text='EOptionSelector',
                 styleCode='',
                 var=None, 
                 Options=['Option #1', 'Option #2', 'Option #3'], 
                 placeMent=EPlace(10,10),
                 textCompund=tk.TOP,
                 textSpace=0,
                 toolTip=ETip('EOptionSelector')):

    ## Vars ##
        self.textCompund = textCompund
        self.textSpace   = textSpace
        self.text    = text
        self.m       = master
        self.tip     = toolTip
        self.command = None
        self.Options = Options
        self.Options.insert(0,self.Options[0])
        self.placeMent = placeMent
        self.style   = EStyle(styleCode)
        if var == None: self.var = tk.StringVar(self.m)
        else: self.var = var
        self.var.set(Options[1]); 
        self.Options = Options
        borderThick = int(self.style.border_thick)

    ## Border ##
        if self.placeMent.width != None and self.placeMent.height != None:
            self.border = tk.Frame(master, 
                                   bg=self.style.border_color, bd=0, 
                                   width =self.placeMent.width +self.style.border_thick*2, 
                                   height=self.placeMent.height+self.style.border_thick*2)
        else:
            self.border = tk.Frame(master, 
                                   bg=self.style.border_color, bd=0, 
                                   width =self.style.border_thick*2, 
                                   height=self.style.border_thick*2)

    ## Widget ##
        super().__init__(master, self.var, *self.Options,style='my.TMenubutton',command=self.__func)
        
    ## Style ##
        #self.configure(indicatoron=0, compound=tk.RIGHT)
        self.s = ttk.Style(master)
        self.s.configure("my.TMenubutton",background=self.style.bg, foreground=self.style.fg,
                            activebackground=self.style.active_bg,font=(self.style.font.family, self.style.font.size, self.style.font.type),
                            compound=tk.RIGHT,indicatoron=0)
        self.s.layout("my.TMenubutton")
        self['menu'].config(bg=self.style.menu_bg, activebackground=self.style.menu_active_bg, fg=self.style.menu_fg, 
                                    activeforeground=self.style.menu_active_fg)
        
        if self.style.arrow_color == 'black': self.configure(image=EImage(os.path.join(FolderETK,'Data\\BA.png')))
        if self.style.arrow_color == 'white': self.configure(image=EImage(os.path.join(FolderETK,'Data\\WA.png')))
        
        
    ## Place ##
        self.place(x         =self.placeMent.x        , 
                   y         =self.placeMent.y        , 
                   relx      =self.placeMent.relx     , 
                   rely      =self.placeMent.rely     , 
                   width     =self.placeMent.width    , 
                   height    =self.placeMent.height   , 
                   relwidth  =self.placeMent.relwidth , 
                   relheight =self.placeMent.relheight)
        master.update()
        if self.placeMent.width == None and self.placeMent.height == None:
            self.border.configure(width =self.winfo_width ()+int(self.style.border_thick)*2, 
                                  height=self.winfo_height()+int(self.style.border_thick)*2)

        self.border.place(x         =int(self.placeMent.x-int(self.style.border_thick)), 
                          y         =int(self.placeMent.y-int(self.style.border_thick)), 
                          relx      =self.placeMent.relx, 
                          rely      =self.placeMent.rely, 
                          relwidth  =self.placeMent.relwidth, 
                          relheight =self.placeMent.relheight)

        if textCompund == tk.LEFT:
            self.label = EStaticText(master,text,styleCode=f'bg:{self.m["bg"]}',
                                    placeMent=EPlace((placeMent.x+(self.winfo_width()+borderThick*4))+textSpace,
                                                      placeMent.y+(self.winfo_height/2)),
                              toolTip=ETip(self.tip.text,delay=self.tip.delay,followMouse=self.tip.follwMouse,toolTipSwitch=self.tip.toolTipSwitch))
        if textCompund == tk.RIGHT:
            self.label = EStaticText(master,text,styleCode=f'bg:{self.m["bg"]}',
                                    placeMent=EPlace((placeMent.x-borderThick*4)-textSpace,
                                                      placeMent.y+(self.winfo_height/2)),
                              toolTip=ETip(self.tip.text,delay=self.tip.delay,followMouse=self.tip.follwMouse,toolTipSwitch=self.tip.toolTipSwitch))
        if textCompund == tk.TOP:
            self.label = EStaticText(master,text,styleCode=f'bg:{self.m["bg"]}',
                                    placeMent=EPlace( placeMent.x-2,
                                                      placeMent.y-(self.winfo_height())-textSpace),
                              toolTip=ETip(self.tip.text,delay=self.tip.delay,followMouse=self.tip.follwMouse,toolTipSwitch=self.tip.toolTipSwitch))
        if textCompund == tk.BOTTOM:
            self.label = EStaticText(master,text,styleCode=f'bg:{self.m["bg"]}',
                                    placeMent=EPlace( placeMent.x-2,
                                                     (placeMent.y+(self.winfo_height()+borderThick))+textSpace),
                              toolTip=ETip(self.tip.text,delay=self.tip.delay,followMouse=self.tip.follwMouse,toolTipSwitch=self.tip.toolTipSwitch))                                   
        self.label.config(fg=self.style.fg)
        self.toolTip=EToolTip(self,self.tip.text,delay=self.tip.delay,followMouse=self.tip.follwMouse,toolTipSwitch=self.tip.toolTipSwitch)
    
    def __func(self,x):
        if self.command != None:
            self.command(x)
        ## Border Place ##
        self.m.update()
        if self.placeMent.width == None and self.placeMent.height == None:
            self.border.configure(width =self.winfo_width ()+int(self.style.border_thick)*2, 
                                  height=self.winfo_height()+int(self.style.border_thick)*2)

        self.border.place(x         =int(self.placeMent.x-int(self.style.border_thick)), 
                          y         =int(self.placeMent.y-int(self.style.border_thick)), 
                          relx      =self.placeMent.relx, 
                          rely      =self.placeMent.rely, 
                          relwidth  =self.placeMent.relwidth, 
                          relheight =self.placeMent.relheight)
    
    def rePaint(self) -> None:
        ## Place ##
        self.m.update()
        if self.placeMent.width == None and self.placeMent.height == None:
            self.border.configure(width =self.winfo_width ()+int(self.style.border_thick)*2, 
                                  height=self.winfo_height()+int(self.style.border_thick)*2)

        self.border.place(x         =int(self.placeMent.x-int(self.style.border_thick)), 
                          y         =int(self.placeMent.y-int(self.style.border_thick)), 
                          relx      =self.placeMent.relx, 
                          rely      =self.placeMent.rely, 
                          relwidth  =self.placeMent.relwidth, 
                          relheight =self.placeMent.relheight)

    def getOptions(self):
        return self.Options[1:]
    
    def __update(self):
        ## Place ##
        self.place(x         =self.placeMent.x        , 
                   y         =self.placeMent.y        , 
                   relx      =self.placeMent.relx     , 
                   rely      =self.placeMent.rely     , 
                   width     =self.placeMent.width    , 
                   height    =self.placeMent.height   , 
                   relwidth  =self.placeMent.relwidth , 
                   relheight =self.placeMent.relheight)
        self.m.update()
        if self.placeMent.width == None and self.placeMent.height == None:
            self.border.configure(width =self.winfo_width ()+int(self.style.border_thick)*2, 
                                  height=self.winfo_height()+int(self.style.border_thick)*2)

        self.border.place(x         =int(self.placeMent.x-int(self.style.border_thick)), 
                          y         =int(self.placeMent.y-int(self.style.border_thick)), 
                          relx      =self.placeMent.relx, 
                          rely      =self.placeMent.rely, 
                          relwidth  =self.placeMent.relwidth, 
                          relheight =self.placeMent.relheight)
        self['menu'].config(bg=self.style.menu_bg, activebackground=self.style.menu_active_bg, fg=self.style.menu_fg, 
                                    activeforeground=self.style.menu_active_fg)
        
        if self.style.arrow_color == 'black': self.configure(image=EImage(os.path.join(FolderETK,'Data\\BA.png')))
        if self.style.arrow_color == 'white': self.configure(image=EImage(os.path.join(FolderETK,'Data\\WA.png')))

    def addOption(self,option):
        self.Options.append(option)
        self.destroy()
        super().__init__(self.m, self.var, *self.Options,style='my.TMenubutton',command=self.__func)
        self.__update()
    
    def removeOption(self,option):
        self.Options.remove(option)
        self.destroy()
        super().__init__(self.m,self.var,*self.Options,style='my.TMenubutton',command=self.__func)
        self.__update()
    
    def onSelect(self,func):
        self.command = func

class EColorPick(object):
    def __init__(self, 
                 master, 
                 defaultColor=(0,255,10), 
                 allowAlpha=False, 
                 titleWindow="EColorPick",
                 text="PickColor",
                 placeMent=EPlace(0,0),
                 toolTip=ETip('Pick your color.'), 
                 styleCode='bg : #242424, fg : white, border-thick:0px'):
        
        self.master       = master
        self.defaultColor = defaultColor
        self.allowAlpha   = allowAlpha
        self.titleWindow  = titleWindow
        self.color        = None
        self.placeMent    = placeMent

        # Pick Color Button
        self.btn = EButton(master,text,styleCode=styleCode,placeMent=placeMent,
                           toolTip=toolTip,command=self.showWindow)
        EI.createCurnerImage('c:\\Windows\\Temp\\color.png',color=self.defaultColor)
        if self.placeMent.width == None and self.placeMent.height == None:
            self.btn.setImage(EImage('c:\\Windows\\Temp\\color.png',"X:64,Y:64"))
        if self.placeMent.width == None and self.placeMent.height != None:
            self.btn.setImage(EImage('c:\\Windows\\Temp\\color.png',f"X:64,Y:{self.placeMent.height-5}"))
        if self.placeMent.width != None and self.placeMent.height == None:
            self.btn.setImage(EImage('c:\\Windows\\Temp\\color.png',f"X:{self.placeMent.width-5},Y:64"))
        else:
            self.btn.setImage(EImage('c:\\Windows\\Temp\\color.png',f"X:{self.placeMent.width-5},Y:{self.placeMent.height-(self.btn.style.font.size+5)}"))

    def getColor(self):
        return self.color
    
    def getHEX(self):
        return self.color[1]
    
    def getRGB(self):
        return self.color[0]
    
    def showWindow(self):
        self.color = askcolor(self.defaultColor, parent=self.master, title=self.titleWindow, alpha=self.allowAlpha)
        EI.createCurnerImage('c:\\Windows\\Temp\\color.png',color=self.color[1])
        if self.placeMent.width == None and self.placeMent.height == None:
            self.btn.setImage(EImage('c:\\Windows\\Temp\\color.png',"X:64,Y:64"))
        if self.placeMent.width == None and self.placeMent.height != None:
            self.btn.setImage(EImage('c:\\Windows\\Temp\\color.png',f"X:64,Y:{self.placeMent.height-5}"))
        if self.placeMent.width != None and self.placeMent.height == None:
            self.btn.setImage(EImage('c:\\Windows\\Temp\\color.png',f"X:{self.placeMent.width-5},Y:64"))
        else:
            self.btn.setImage(EImage('c:\\Windows\\Temp\\color.png',f"X:{self.placeMent.width-5},Y:{self.placeMent.height-(self.btn.style.font.size+5)}"))
    
    def showWindowGetColor(self):
        self.color = askcolor(self.defaultColor, parent=self.master, title=self.titleWindow, alpha=self.allowAlpha)
        return self.color

class ESquare(tk.Frame):
    def __init__(self, 
                master, 
                color       = 'red', 
                styleCode   = 'fg:white,border-color:grey,border-thick:3px',
                placeMent   = EPlace(10,10), 
                image       = None,
                text        = None,
                textCompund = tk.BOTTOM,
                textSpace   = 1,
                toolTip=ETip('ESquare')):
        
        self.mag         = placeMent
        self.placeMent   = placeMent
        self.m           = master
        self.style       = EStyle(styleCode)
        self.borderThick = int(self.style.border_thick) 
        borderThick      = self.borderThick
        self.master      = master; 
        self.size        = (placeMent.width,placeMent.height)
        self.tip         = toolTip

        self.SY = {'X' :placeMent.x,
                   'Y' :placeMent.y,
                   'rh':placeMent.relheight,
                   'rw':placeMent.relwidth,
                   'rx':placeMent.relx,
                   'ry':placeMent.rely
                   }
        
        if self.placeMent.width != None and self.placeMent.height != None:
            self.border = tk.Frame(master, 
                                   bg=self.style.border_color, 
                                   bd=0, 
                                   width=self.placeMent.width+self.style.border_thick*2, 
                                   height=self.placeMent.height+self.style.border_thick*2
                                   )
        else:
            self.border = tk.Frame(master, 
                                   bg=self.style.border_color, 
                                   bd=0, 
                                   width =self.style.border_thick*2, 
                                   height=self.style.border_thick*2
                                   )

        super().__init__(master, bg=color)

        self.place(x=self.SY['X'], 
                   y=self.SY['Y'], 
                   relheight=self.SY['rh'], 
                   relwidth=self.SY['rw'], 
                   relx=self.SY['rx'], 
                   rely=self.SY['ry'], 
                   width =self.size[0], 
                   height=self.size[1]
                   )
        master.update()

        if self.mag.width == None and self.mag.height == None:
            self.border.configure(width =self.winfo_width()+int(self.style.border_thick)*2, 
                                  height=self.winfo_height()+int(self.style.border_thick)*2)
        self.border.place(x=int(self.mag.x-int(self.style.border_thick)), 
                          y=int(self.mag.y-int(self.style.border_thick)), 
                          relx=self.mag.relx, 
                          rely=self.mag.rely, 
                          relwidth=self.mag.relwidth, 
                          relheight=self.mag.relheight
                          )
        selfImg = EStaticText(self, text='',
                              styleCode=f'bg:{color}',
                              placeMent=EPlace(0,0,relx=0.5,rely=0.5),
                              toolTip=ETip(self.tip.text,delay=self.tip.delay,followMouse=self.tip.follwMouse,toolTipSwitch=self.tip.toolTipSwitch)
                             )
        selfImg.setImage(image)
        if textCompund == tk.LEFT:
            self.label = EStaticText(master,text,styleCode=f'bg:{self.m["bg"]}',
                                    placeMent=EPlace((placeMent.x+(self.winfo_width()+borderThick*4))+textSpace,
                                                      placeMent.y+(self.winfo_height/2)),
                                    toolTip=ETip(self.tip.text,delay=self.tip.delay,followMouse=self.tip.follwMouse,toolTipSwitch=self.tip.toolTipSwitch))
        if textCompund == tk.RIGHT:
            self.label = EStaticText(master,text,styleCode=f'bg:{self.m["bg"]}',
                                    placeMent=EPlace((placeMent.x-borderThick*4)-textSpace,
                                                      placeMent.y+(self.winfo_height/2)),
                                    toolTip=ETip(self.tip.text,delay=self.tip.delay,followMouse=self.tip.follwMouse,toolTipSwitch=self.tip.toolTipSwitch))
        if textCompund == tk.TOP:
            self.label = EStaticText(master,text,styleCode=f'bg:{self.m["bg"]}',
                                    placeMent=EPlace( placeMent.x-2,
                                                      placeMent.y-(self.winfo_height())-textSpace),
                                    toolTip=ETip(self.tip.text,delay=self.tip.delay,followMouse=self.tip.follwMouse,toolTipSwitch=self.tip.toolTipSwitch)) 
        if textCompund == tk.BOTTOM:
            self.label = EStaticText(master,text,styleCode=f'bg:{self.m["bg"]}',
                                    placeMent=EPlace( placeMent.x-2,
                                                     (placeMent.y+(self.winfo_height()+borderThick))+textSpace),
                                    toolTip=ETip(self.tip.text,delay=self.tip.delay,followMouse=self.tip.follwMouse,toolTipSwitch=self.tip.toolTipSwitch))                                   
        self.label.config(fg=self.style.fg)
        self.toolTip = EToolTip(self,self.tip.text,delay=self.tip.delay,followMouse=self.tip.follwMouse,toolTipSwitch=self.tip.toolTipSwitch)

    def hideWidget(self):
        self.place_forget()
        self.border.place_forget()

    def showWidget(self):
        self.place(x=self.SY['X'], 
                   y=self.SY['Y'], 
                   relheight=self.SY['rh'], 
                   relwidth=self.SY['rw'], 
                   relx=self.SY['rx'], 
                   rely=self.SY['ry'], 
                   width=self.Size[0], 
                   height=self.Size[1]
                   )
        self.updateBorderStatement()
    
    def updateBorderStatement(self):
        self.master.update()
        if self.borderThick != 0:
            if self.SY['rh'] != 0 and self.SY['rw'] == None:
                self.border.configure(width=self.winfo_width()+self.borderThick*2)
                self.border.place(x=int(self.SY['X']-self.borderThick), 
                                  y=int(self.SY['Y']-self.borderThick), 
                                  relx=self.SY['rx'], 
                                  rely=self.SY['ry'], 
                                  relwidth=self.SY['rw'], 
                                  relheight=self.SY['rh'], 
                                  height=self.winfo_height()-(470+self.borderThick)
                                  )

            elif self.SY['rh'] != 0 and self.SY['rw'] == None:
                self.border.configure(height=self.winfo_height()+self.borderThick*2)
                self.border.place(x=int(self.SY['X']-self.borderThick), 
                                  y=int(self.SY['Y']-self.borderThick), 
                                  relx=self.SY['rx'], 
                                  rely=self.SY['ry'], 
                                  relwidth=self.SY['rw'], 
                                  relheight=self.SY['rh'], 
                                  width=self.winfo_width()-(470+self.borderThick)
                                  )

            elif self.SY['rh'] != 0 and self.SY['rw'] != None:
                self.border.place(x=int(self.SY['X']-self.borderThick), 
                                  y=int(self.SY['Y']-self.borderThick), 
                                  relx=self.SY['rx'], 
                                  rely=self.SY['ry'], 
                                  relwidth=self.SY['rw'], 
                                  relheight=self.SY['rh'], 
                                  width=self.winfo_width()-(470+self.borderThick),
                                  height=self.winfo_height()-(470+self.borderThick)
                                  )

            else:
                self.border.configure(width =self.winfo_width()+self.borderThick*2,
                                      height=self.winfo_height()+self.borderThick*2)
                self.border.place(x=int(self.SY['X']-self.borderThick), 
                                  y=int(self.SY['Y']-self.borderThick), 
                                  relx=self.SY['rx'], 
                                  rely=self.SY['ry'], 
                                  relwidth=self.SY['rw'], 
                                  relheight=self.SY['rh']
                                  )

class ETreeView(ttk.Treeview):
    def __init__(self,
                 master,
                 styleCode='', 
                 placeMent=EPlace(10, 10),
                 toolTip=ETip(text='ETreeView', delay=300),
                 data={},
                 text='Browse Objects:',
                 textCompund=tk.TOP,
                 textSpace=5
                ):

        self.m           = master
        self.styleleCode = styleCode
        self.style       = EStyle(self.styleleCode)
        self.placeMent   = placeMent
        self.tip         = toolTip
        self.data        = data
        borderThick      = int(self.style.border_thick)

    ## Border ##
        if self.placeMent.width != None and self.placeMent.height != None:
            self.border = tk.Frame(master, 
                                   bg=self.style.border_color, bd=0, 
                                   width =self.placeMent.width +self.style.border_thick*2, 
                                   height=self.placeMent.height+self.style.border_thick*2)
        else:
            self.border = tk.Frame(master, 
                                   bg=self.style.border_color, bd=0, 
                                   width =self.style.border_thick*2, 
                                   height=self.style.border_thick*2)

    ## Style ##
        self.s = ttk.Style(master)
        self.s.configure("s.Treeview",background=self.style.bg, foreground=self.style.fg,
                          activebackground=self.style.active_bg,compound=tk.LEFT,
                          font=(self.style.font.family, self.style.font.size, self.style.font.type))
        self.s.layout("s.Treeview")
        self.s.theme_use('clam')
    
    ## Widget ##
        super().__init__(master,style="s.Treeview")

    ## Place ##
        self.place(x         =self.placeMent.x        , 
                   y         =self.placeMent.y        , 
                   relx      =self.placeMent.relx     , 
                   rely      =self.placeMent.rely     , 
                   width     =self.placeMent.width    , 
                   height    =self.placeMent.height   , 
                   relwidth  =self.placeMent.relwidth , 
                   relheight =self.placeMent.relheight)
        master.update()
        self.border.configure(width =self.winfo_width ()+int(self.style.border_thick)*2, 
                              height=self.winfo_height()+int(self.style.border_thick)*2)
        self.border.place(x         =int(self.placeMent.x-int(self.style.border_thick)), 
                          y         =int(self.placeMent.y-int(self.style.border_thick)), 
                          relx      =self.placeMent.relx, 
                          rely      =self.placeMent.rely, 
                          relwidth  =self.placeMent.relwidth, 
                          relheight =self.placeMent.relheight)

        if textCompund == tk.LEFT:
            self.label = EStaticText(master,text,styleCode=f'bg:{self.m["bg"]}',
                                    placeMent=EPlace((placeMent.x+(self.winfo_width()+borderThick*4))+textSpace,
                                                      placeMent.y+(self.winfo_height/2)),
                              toolTip=ETip(self.tip.text,delay=self.tip.delay,followMouse=self.tip.follwMouse,toolTipSwitch=self.tip.toolTipSwitch))
        if textCompund == tk.RIGHT:
            self.label = EStaticText(master,text,styleCode=f'bg:{self.m["bg"]}',
                                    placeMent=EPlace((placeMent.x-borderThick*4)-textSpace,
                                                      placeMent.y+(self.winfo_height/2)),
                              toolTip=ETip(self.tip.text,delay=self.tip.delay,followMouse=self.tip.follwMouse,toolTipSwitch=self.tip.toolTipSwitch))
        if textCompund == tk.TOP:
            self.label = EStaticText(master,text,styleCode=f'bg:{self.m["bg"]}',
                                    placeMent=EPlace( placeMent.x-2,
                                                      placeMent.y-(self.winfo_height())-textSpace),
                              toolTip=ETip(self.tip.text,delay=self.tip.delay,followMouse=self.tip.follwMouse,toolTipSwitch=self.tip.toolTipSwitch))
        if textCompund == tk.BOTTOM:
            self.label = EStaticText(master,text,styleCode=f'bg:{self.m["bg"]}',
                                    placeMent=EPlace( placeMent.x-2,
                                                     (placeMent.y+(self.winfo_height()+borderThick))+textSpace),
                              toolTip=ETip(self.tip.text,delay=self.tip.delay,followMouse=self.tip.follwMouse,toolTipSwitch=self.tip.toolTipSwitch))                                   
        self.label.config(fg=self.style.fg)
        self.toolTip     = EToolTip(self,self.tip.text,delay=self.tip.delay,followMouse=self.tip.follwMouse,toolTipSwitch=self.tip.toolTipSwitch)
        self.items       = []
        self.itemText    = []
        self.parentItems = []
        self.tags        = []

    def getData(self) -> dict:
        return self.data
    
    def __update(self) -> None:
        ## Place ##
        self.place(x         =self.placeMent.x        , 
                   y         =self.placeMent.y        , 
                   relx      =self.placeMent.relx     , 
                   rely      =self.placeMent.rely     , 
                   width     =self.placeMent.width    , 
                   height    =self.placeMent.height   , 
                   relwidth  =self.placeMent.relwidth , 
                   relheight =self.placeMent.relheight)
        self.m.update()
        if self.placeMent.width == None and self.placeMent.height == None:
            self.border.configure(width =self.winfo_width ()+int(self.style.border_thick)*2, 
                                  height=self.winfo_height()+int(self.style.border_thick)*2)

        self.border.place(x         =int(self.placeMent.x-int(self.style.border_thick)), 
                          y         =int(self.placeMent.y-int(self.style.border_thick)), 
                          relx      =self.placeMent.relx, 
                          rely      =self.placeMent.rely, 
                          relwidth  =self.placeMent.relwidth, 
                          relheight =self.placeMent.relheight)

    def addItem(self,item:str,values:dict,tags='item') -> None:
        #try:
            toSet = []
            for i in self.data.keys():
                toSet.append(values[i])
                self.data[i].append(values[i])
            self.itemText.append(item)
            print(toSet)
            tag = tags+str(self.itemText.index(item))
            self.tags.append(tag)
            self.items.append(self.insert('', 'end', text=item, values=tuple(toSet),tags=(tag)))
            del toSet
            self.__update()
        #except:
            #pass

    def addParentItem(self,item:str,parentItem:str,values:dict,tags='item') -> None:
            toSet = []
            for i in self.data.keys():
                toSet.append(values[i])
                self.data[i].append(values[i])
            self.itemText.append(item)
            print(toSet)
            tag = tags+str(self.itemText.index(item))
            self.tags.append(tag)
            self.items.append(self.insert(self.items[self.itemText.index(parentItem)], 'end', text=item, values=tuple(toSet),tags=(tag)))
            del toSet
            self.__update()

    def setColumns(self,columns:tuple) -> None:
        self["columns"] = columns
        self.column ("#0", width=10,minwidth=10,stretch=tk.YES)
        self.heading("#0", text=" ",anchor=tk.W)
        for i in columns:
            self.column(i,stretch=tk.YES)
            self.heading(i,text=i,anchor=tk.W)
            self.data[i] = []

    def removeItem(self,item:str):
        print(self.get_children())
    
    def chessTheme(self) -> None:
        for i in range(len(self.tags)):
            print(self.tags[i])
            if int(i%2) == 0:
                self.tag_configure(self.tags[i],background='#E8E8E8')
            if int(i%2) == 1:
                self.tag_configure(self.tags[i],background='#DFDFDF')


