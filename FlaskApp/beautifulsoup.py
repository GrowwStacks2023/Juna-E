import tidylib

def tidy_html(input_html):
    clean_html, errors = tidylib.tidy_document(input_html, options={'numeric-entities': 1})
    return clean_html

# Example
broken_html = """<span style="color: red;">SR: admin@growwstacks.com </span>
<br />
<span style="color: blue;">TO: 4319@emailbyfax.org</span>
<br />
<span style="color: green;">CC: </span>
<br />
<span style="color: purple;">TM: 07:26 AM
 </span>
<br />
<br />


 

<div dir="ltr"><table role="presentation" cellspacing="0" cellpadding="10" border="0" width="100%" class="gmail-x_paragraph_block gmail-x_block-3" style="font-variant-numeric:inherit;font-variant-east-asian:inherit;font-variant-alternates:inherit;font-stretch:inherit;font-size:15px;line-height:inherit;font-size-adjust:inherit;font-kerning:inherit;font-feature-settings:inherit;color:rgb(0,0,0);background-color:rgb(252,252,252);word-break:break-word"><tbody style="box-sizing:border-box"><tr style="box-sizing:border-box"><td class="gmail-x_pad" style="box-sizing:border-box"><div style="border:0px;font-style:inherit;font-variant:inherit;font-stretch:inherit;font-size:16px;line-height:24px;font-family:&quot;Source Sans Pro&quot;,Tahoma,Verdana,Segoe,sans-serif,serif,EmojiFont;font-size-adjust:inherit;font-kerning:inherit;font-feature-settings:inherit;margin:0px;padding:0px;vertical-align:baseline;box-sizing:border-box;direction:ltr;letter-spacing:0px"><p style="box-sizing:border-box;line-height:inherit;margin:0px 0px 16px">In partnership with Andrew Ng&#39;s DeepLearningAI, this course covers everything you need to know about vibe coding:</p><p style="box-sizing:border-box;line-height:inherit;margin:0px 0px 16px">1️⃣ Tips for making the most of Replit&#39;s AI tools</p><p style="box-sizing:border-box;line-height:inherit;margin:0px 0px 16px">2️⃣ Practical strategies for building amazing apps</p><p style="box-sizing:border-box;line-height:inherit;margin:0px 0px 16px">3️⃣ How you can go from idea to live app in minutes</p><p style="box-sizing:border-box;line-height:inherit;margin:0px">All through project-based lessons with a simple, hands-on approach.</p></div></td></tr></tbody></table><table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" class="gmail-x_image_block gmail-x_block-4" style="font-variant-numeric:inherit;font-variant-east-asian:inherit;font-variant-alternates:inherit;font-stretch:inherit;font-size:15px;line-height:inherit;font-size-adjust:inherit;font-kerning:inherit;font-feature-settings:inherit;color:rgb(0,0,0);background-color:rgb(252,252,252)"><tbody style="box-sizing:border-box"><tr style="box-sizing:border-box"><td width="100%" class="gmail-x_pad" style="box-sizing:border-box;width:540px"><div align="center" class="gmail-x_alignment" style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;font-stretch:inherit;font-size:inherit;line-height:10px;font-family:inherit;font-size-adjust:inherit;font-kerning:inherit;font-feature-settings:inherit;margin:0px;padding:0px;vertical-align:baseline;color:inherit;box-sizing:border-box"><div style="border:0px;font:inherit;margin:0px;padding:0px;vertical-align:baseline;color:inherit;box-sizing:border-box;max-width:540px"><img height="auto" title="" alt="" width="540" style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit; box-sizing: border-box; display: block; height: auto; width: 540px;"></div></div></td></tr></tbody></table><table role="presentation" cellspacing="0" cellpadding="10" border="0" width="100%" class="gmail-x_paragraph_block gmail-x_block-5" style="font-variant-numeric:inherit;font-variant-east-asian:inherit;font-variant-alternates:inherit;font-stretch:inherit;font-size:15px;line-height:inherit;font-size-adjust:inherit;font-kerning:inherit;font-feature-settings:inherit;color:rgb(0,0,0);background-color:rgb(252,252,252);word-break:break-word"><tbody style="box-sizing:border-box"><tr style="box-sizing:border-box"><td class="gmail-x_pad" style="box-sizing:border-box"><div style="border:0px;font-style:inherit;font-variant:inherit;font-stretch:inherit;font-size:16px;line-height:24px;font-family:&quot;Source Sans Pro&quot;,Tahoma,Verdana,Segoe,sans-serif,serif,EmojiFont;font-size-adjust:inherit;font-kerning:inherit;font-feature-settings:inherit;margin:0px;padding:0px;vertical-align:baseline;box-sizing:border-box;direction:ltr;letter-spacing:0px"><p style="box-sizing:border-box;line-height:inherit;margin:0px">The course is taught by Replit&#39;s President, <a href="https://links.replit.com/s/c/1Q8_9t5pNQmuOTD3eE8ieIWUIBIXZJasu-TIsc__UcSD0YSUxHXpc_5ftXQ6XG5I0zpPSNl4WMK44Bd6zXIQSvIit5_zH6dJavdi-84AxNDAg-3eKXoFjYepagrLJnXiSf2fi4JMDNfzY3A-4CQ4N9RDlqhBFLgqIqIu_heC3pLeOk7YOG-yQv0gyRe4U-Jani3oGxluxRis-2r3altg0gXiVPuL9DM-1YJtCf_D180kfKlOofJn004ifzInROdr8Pjp98sCoyncZqgtuW_vCw2vJZ6smZvxxlCRBMGI4SCpaWnOGd2nhzYJu41A8znS0AeYEx6ZIl4fVnNsuCh1syP5W10WhDWpZX4yF1EYNz_3e-V9ANRQdhM/F5lQcofQOMjYYBgtuTiPX6nUCiquUdSY/7" title="https://links.replit.com/s/c/1Q8_9t5pNQmuOTD3eE8ieIWUIBIXZJasu-TIsc__UcSD0YSUxHXpc_5ftXQ6XG5I0zpPSNl4WMK44Bd6zXIQSvIit5_zH6dJavdi-84AxNDAg-3eKXoFjYepagrLJnXiSf2fi4JMDNfzY3A-4CQ4N9RDlqhBFLgqIqIu_heC3pLeOk7YOG-yQv0gyRe4U-Jani3oGxluxRis-2r3altg0gXiVPuL9DM-1YJtCf_D180kfKlOofJn004ifzInROdr8Pjp98sCoyncZqgtuW_vCw2vJZ6smZvxxlCRBMGI4SCpaWnOGd2nhzYJu41A8znS0AeYEx6ZIl4fVnNsuCh1syP5W10WhDWpZX4yF1EYNz_3e-V9ANRQdhM/F5lQcofQOMjYYBgtuTiPX6nUCiquUdSY/7" style="border:0px;font:inherit;margin:0px;padding:0px;vertical-align:baseline;box-sizing:border-box;color:rgb(0,104,165)">Michele Catasta</a>, and me (Matt). We had a blast recording it— we hope you have just as much fun following along.</p><img src="cid:ii_m8r9oi7s0" alt="image.png" width="542" height="78"><br></div></td></tr></tbody></table></div><style type="text/css">  @page {
    size: A4;
    margin: 0;
}
html, body {
    width: 100% !important;
    height: auto;
    margin: 0; 
    padding: 0;
    box-sizing: border-box;
    overflow-x: hidden; 
}

table,div {
    width: 100% !important;
    max-width: 100% !important;
}
p, td, th {
    margin: 0;
    padding: 0;
}"""
fixed_html = tidy_html(broken_html)
print(fixed_html)