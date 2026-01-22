# Midnight-Media-Downloader

I got real tired of websites full of ads, risk for viruses, scams, info snatchers and what not, so i made this simple media downloader in python that should work with most, if not all media links, even the more non-conventional ones if you know what you are doing.
I want and shall maintain this for as long as i can and as long as i can think of something to add/fix, i'm no expert, just some dude trying to improve (i think you can tell by my shit readme).

#DEPENDENCIES

To be able to use this without issues you will need:

    ffmpeg-python (https://github.com/kkroening/ffmpeg-python)
    yt-dlp (https://github.com/yt-dlp/yt-dlp)
    A full corret instalation of ffmpeg

#INSTRUCTIONS

Honestly, it's pretty intuitive, but a few warnings just in case:

    -If your link is from a average/conventional/social media one, please mark the checkbox that says "Social Media Link",
     because (AS FAR AS MY LITTLE KNOWLEDGE GOES) ffmpeg can't just fetch the media in those link (youtube for example)

    -If you have an nvidia graphics card, i strongly recomend that you check the mark that says Use Nvidia GPU (Video Only),
     because i made it able to use the hardware acceleration from nvidia. The difference is not abysmal, but it gets the job done.

#FINAL NOTES

Any feedback, suguestions or issues that you may have, plase let me know, i wish to improve both my skills and this... abomination. Also, if any experienced devs wish to roast me or my code, do so, i know this is isn't great and honetly i would find it funny, cheers.

#LINUX USERS

Clone the repo as you normally would and start a python venv.
Install Customtkinter, yt-dlp and ffmpeg.
Start Downloader.py and you should be fine, please open a ticket if something doesn't work.
