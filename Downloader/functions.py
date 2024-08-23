import ffmpeg as fmp
import yt_dlp as yt

class Funtions_avg:
    
    def download_mp4(self,url:str,file_name:str,quality:str):
        match quality:
            case "Fast (low quality)":
                v_bitrate = '5M'
                
            case "Medium (default)":
                v_bitrate = '10M'
                
            case "Slow (best quality)":
                v_bitrate = '15M'
        
        try:
            input_file = url
            output_file = file_name + ".mp4"
            stream = fmp.input(input_file)
            download = fmp.output(stream,output_file,format='mp4',video_bitrate=v_bitrate)
            fmp.run_async(download)
        except Exception as e:
            print(e)
            
        
    def download_mp3(self,url:str,file_name:str,quality:str):
        
        match quality:
            case "Fast (low quality)":
                a_bitrate = '96k'
                
            case "Medium (default)":
                a_bitrate = '128k'
                
            case "Slow (best quality)":
                a_bitrate = '196k'
        
        try:
            input_file = url
            output_file = file_name + ".mp3"
            stream = fmp.input(input_file)
            download = fmp.output(stream,output_file,format='mp3',audio_bitrate=a_bitrate)
            fmp.run_async(download)
        except Exception as e:
            print(e)
        
    def download_wav(self,url:str,file_name:str,quality:str):
        
        match quality:
            case "Fast (low quality)":
                a_bitrate = '96k'
                
            case "Medium (default)":
                a_bitrate = '128k'
                
            case "Slow (best quality)":
                a_bitrate = '196k'
        
        try:
            input_file = url
            output_file = file_name + ".wav"
            stream = fmp.input(input_file)
            download = fmp.output(stream,output_file,format='wav',audio_bitrate=a_bitrate)
            fmp.run_async(download)
        except Exception as e:
            print(e)
            
            
    def social_media_download_mp4(self,url:str,file_name:str):
        
        try:
            input_url = url
            output_file = file_name + ".mp4"
            ydl_opts = {
                "format": 'best',
                "outtmpl": output_file,
            }
            with yt.YoutubeDL(ydl_opts) as ydl:
                ydl.download([input_url])
        except Exception as e:
            print(e)
            
    def social_media_download_mp3(self,url:str,file_name:str):
        
        try:
            input_url = url
            output_file = file_name + ".mp3"
            ydl_opts = {
                "format": 'bestaudio/best',
                "outtmpl": output_file,
                "postprocessors": [{
                    'key':'FFmpegExtractAudio',
                    "preferredcodec":'mp3'
                }]
            }
            with yt.YoutubeDL(ydl_opts) as ydl:
                ydl.download([input_url])
        except Exception as e:
            print(e)
            
    def social_media_download_wav(self,url:str,file_name:str):
        
        try:
            input_url = url
            output_file = file_name + ".wav"
            ydl_opts = {
                "format": 'bestaudio/best',
                "outtmpl": output_file,
                "postprocessors": [{
                    'key':'FFmpegExtractAudio',
                    "preferredcodec":'wav'
                }]
            }
            with yt.YoutubeDL(ydl_opts) as ydl:
                ydl.download([input_url])
        except Exception as e:
            print(e)
            
class Funtions_nvidia:
    
    def download_mp4(self,url:str,file_name:str,n_profile:str):
        
        try:
            input_file = url
            output_file = file_name + ".mp4"
            stream = fmp.input(input_file,hwaccel='cuda')
            download = fmp.output(stream,output_file,format='mp4',vcodec='h264_nvenc',preset=n_profile,video_bitrate='20M')
            fmp.run_async(download)
        except Exception as e:
            print(e)
