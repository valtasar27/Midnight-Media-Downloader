from customtkinter import *
from functions import *
from time import sleep

class Main:
    def __init__(self):
        
        self.root = CTk()
        self.root.title("Midnight Media Downloader")
        set_appearance_mode("Dark")
        self.root.geometry("500x500")
        self.root.resizable(0,0)
        self.root.iconbitmap("icon.ico")
        
        self.mainframe = CTkFrame(master=self.root)
        self.mainframe.pack(fill="both", expand=True)
        
        self.title_font = FontManager.load_font("EduVICWANTBeginner-VariableFont_wght.ttf")
        self.default_font = FontManager.load_font("SourceCodePro-VariableFont_wght.ttf")
        
        self.title = CTkLabel(master=self.mainframe, text="Midnight Media Downloader", font=("Edu VIC WA NT Beginner",30))
        self.title.pack()
        self.title.place(x=90, y=10)
        
        self.link_text = CTkLabel(master=self.mainframe, text="Link", font=("Source Code Pro",13))
        self.link_text.pack()
        self.link_text.place(x=65, y=100)
                
        self.url = CTkEntry(master=self.mainframe, width=300, placeholder_text="URL Here")
        self.url.pack()
        self.url.place(x=105, y=100)
        
        self.social_media_var = IntVar()
        self.social_media = CTkCheckBox(master=self.mainframe, text="Social Media Link",checkbox_width=15, checkbox_height=15, variable= self.social_media_var, command=self.social_media_check)
        self.social_media.pack()
        self.social_media.place(x=105,y=130)

        self.file_name_text = CTkLabel(master=self.mainframe, text="File Name", font=("Source Code Pro",13))
        self.file_name_text.pack()
        self.file_name_text.place(x=27, y=160)
        
        self.file_name = CTkEntry(master=self.mainframe, width=300, placeholder_text="File Name Here")
        self.file_name.pack()
        self.file_name.place(x=105, y=160)
        
        self.format_text = CTkLabel(master=self.mainframe, text="Format", font=("Source Code Pro",13))
        self.format_text.pack()
        self.format_text.place(x=51, y=220)
        
        self.format = CTkComboBox(master=self.mainframe, width=300,state="readonly", values=["MP4","MP3","WAV"])
        self.format.pack()
        self.format.place(x=105, y=220)
        
        self.nvidia_var = IntVar()
        self.nvidia = CTkCheckBox(master=self.mainframe, text="Use Nvidia GPU (Video Only)", checkbox_width=15, checkbox_height=15, variable=self.nvidia_var, command=self.nvidia_cb)
        self.nvidia.pack()
        self.nvidia.place(x=105,y=260)
        
        self.nvidia_text = CTkLabel(master=self.mainframe, text="Quality", font=("Source Code Pro",13))
        self.nvidia_text.pack()
        self.nvidia_text.place(x=45,y=275)
        
        self.nvidia_or_quality_profile = CTkComboBox(master=self.mainframe, width=300, state="readonly", values=["Fast (low quality)","Medium (default)","Slow (best quality)"])
        self.nvidia_or_quality_profile.pack()
        self.nvidia_or_quality_profile.place(x=105,y=280)
              
        self.download_button = CTkButton(master=self.mainframe, width=200, text="Download Video/Audio",font=("Source Code Pro",13), command=self.action_select, border_width=2, border_color="grey")
        self.download_button.pack()
        self.download_button.place(x=150,y=340)
    
    def social_media_check(self):
        if self.social_media_var.get() == 0:
            self.download_button.configure(command=self.action_select)
            
            
        elif self.social_media_var.get() == 1:
            self.download_button.configure(command=self.sm_action_select)
            
            
    def nvidia_cb(self):
        if self.nvidia_var.get() == 0:
            self.format.configure(values=["MP4","MP3","WAV"])
            self.nvidia_text.configure(text="Quality")
            
        elif self.nvidia_var.get() == 1:
            self.format.configure(values=["MP4"])
            self.nvidia_text.configure(text="H264\nProfile")
     
    def sm_action_select(self):
        
        match self.format.get():
            case "MP4":
                Funtions_avg.social_media_download_mp4(self,self.url.get(),self.file_name.get())    
            case "MP3":
                Funtions_avg.social_media_download_mp3(self,self.url.get(),self.file_name.get())
            case "WAV":
                Funtions_avg.social_media_download_wav(self,self.url.get(),self.file_name.get())
        
        
    def action_select(self):
        
        if self.nvidia_var.get() == 0:
            match self.format.get():
                case "MP4":
                    Funtions_avg.download_mp4(self,self.url.get(),self.file_name.get(),self.nvidia_or_quality_profile.get())
                case "MP3":
                    Funtions_avg.download_mp3(self,self.url.get(),self.file_name.get(),self.nvidia_or_quality_profile.get())
                case "WAV":
                    Funtions_avg.download_wav(self,self.url.get(),self.file_name.get(),self.nvidia_or_quality_profile.get())
        
        elif self.nvidia_var.get() == 1:
            match self.nvidia_or_quality_profile.get():
        
                case "Fast (low quality)":
                    Funtions_nvidia.download_mp4(self,self.url.get(),self.file_name.get(),"p3")
                case "Medium (default)":
                    Funtions_nvidia.download_mp4(self,self.url.get(),self.file_name.get(),"p4")
                case "Slow (best quality)":
                    Funtions_nvidia.download_mp4(self,self.url.get(),self.file_name.get(),'p7')
            
    
    def run(self):
        self.root.mainloop()
        
app = Main()

if __name__ == "__main__":
    
    app.run()
