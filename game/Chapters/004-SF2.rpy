# Chapter 4, Straightforward Flashback and Exposition Arc.

label SF2:
    if music_need:
        $ renpy.music.set_volume(0.2, .5, channel="music")
    stop music fadeout 3
    scene black
    show title 004 at card_pos
    with slowfadein
    pause
    play sound "SE/Pageflip3.mp3"
    nvl clear
    
    scene bg KyonRoomRightMorning with fade
    play music "Music/Morning.ogg"
    show Kyon Sigh1 at right
    show Nonoko Smile1 at center with moveinleft
    play sound "SE/impact.mp3"
    show Nonoko Sup1
    "After a brief window of inaction, Kyon awoke to the sensation of impending peril, one hand shooting out from beneath the covers and grasping his sister's descending elbow before she could strike his midsection. \"Urk!\" she whimpered. \"You blocked!?\""
    show Kyon Puzzle1
    "\"Is it time to get up?\" he asked tiredly, sitting up and releasing his sister's arm."
    show Kyon Worry1
    show Nonoko Pout2
    nvl clear
    "She pouted, rubbing at her elbow. \"No,\" she admitted sullenly. \"I got up early to get you up, because it's fun.\""
    show Nonoko Pout1
    show Kyon Smile7
    "He stared at her, then gave a broad grin. \"You're a hundred years too young to try that on me,\" he said defiantly, glancing at his clock and preemptively turning off his alarm."
    show Nonoko Hap1
    show Kyon Smile2
    nvl clear
    "{=loud}\"You win this round!\"{/=loud} his sister cried with mock rage, grinning back and sticking out her tongue. {=loud}\"Next time I'll be the victor!\"{/=loud}"
    show Kyon Sigh2
    show Nonoko Smile1
    "\"I'm sure,\" he answered, knuckling back a yawn and climbing out of bed. \"Come on, let's get cleaned up.\""
    scene black with fade
    nvl clear
    "Despite that initial surge of energy, once he reached the school, Kyon found himself drowsing, continually awoken by Haruhi's mechanical pencil jabbing him in the back just as he was about to drift off."
    nvl clear
    stop music fadeout 3
    
    call eyecatch_fancy("Tuesday, April 19") from SF2_sc001
    
    play music "Music/ItsumoNoFuukei.mp3"
    scene bg classroom with fade:
        size (800,600)
    "Haruhi frowned at the boy in front of her. Why was he so tired? Things were finally getting interesting — really interesting.... Well, she couldn't entirely blame him for trying to ignore the class; he did have better things to think about. But it was no excuse to get a bad grade, especially after all the effort she had put into helping him with his homework."
    "After finishing with the assignments in class, she decided to make a quick study guide, something that would actually make him learn what he'd need for the upcoming test. He might be some kind of hero, but she was the one with the power to reshape reality, and he'd either let her teach him, or she'd persuade Yuki to {i}make{/i} him pay more attention in class."
    "Despite his protestations. He may be in charge of a lot, but he also would need a reminder that she was the supreme commander, and he was just a vice commander."
    nvl clear
    show Kyon Sigh2 at right
    show Haruhi Neutral4 at TenthLeft
    with dissolve
    "\"I am exhausted,\" he declared to no one in particular, when the lunch chime rang."
    show Kyon Sigh4
    show Haruhi Grin2
    "\"Oh? Time traveling?\" she asked him, teasing. \"Maybe fighting off more thugs to protect Tsuruya-san's honor?\""
    show Haruhi Grin1
    "Kunikida paused mid-step as he was about to approach Kyon, then suddenly seemed to think better of it after hearing that remark and moved to an empty seat near Taniguchi."
    nvl clear
    show Kyon Sigh1
    "\"Farewell forever, dear friends,\" Kyon sighed. \"Chased away by fear of Haruhi and being caught up in our madness.\""
    show Kyon Sigh3
    show Haruhi Grin2
    "\"Idiot,\" she retorted, smirking. \"Come on, if you're going to insist we can't talk about important things here, let's go to the clubroom for lunch.\""
    scene bg hallway with wipeleft
    show Kyon Sigh1 at right
    nvl clear
    show Haruhi Smile1 at TenthLeft
    with dissolve
    "\"Naturally,\" he returned, rising to his feet and falling into step beside her. \"There's no way {i}that{/i} comment could be misconstrued.\""
    nvl clear
    show Kyon Sigh3
    show Haruhi Eyeroll2
    "She snorted and gave him a sharp look, but admitted internally that she was pleased. He usually remembered his position, only usurping hers in times of dire emergency, or the occasional times when he ignored her position as his superior entirely and engaged in shameless flirting." 
    "Though that hadn't happened since shortly after Valentine's day, when she thought back on it. Well, it was kind of cute—"
    nvl clear
    show Haruhi Pout1
    show Hblush at TenthLeft
    "She paused, mid-way through pummeling the thought into submission, and made herself face it head on. Alright, she admitted to herself. Kyon could be cute. There was no shame in admitting that, though; even though he was a 'normal' human, it was only on a technical level." 
    nvl clear
    "He didn't have powers, but he was pretty cool. He handled the abnormal with a level head and a placid expression. That was respectable, at least. She nodded decisively."
    show Kyon Puzzle1
    "\"Something on your mind?\" he asked, knuckling back another yawn."
    nvl clear
    hide Hblush
    show Kyon Worry1
    show Haruhi Quest1
    "\"Just wondering why you never have any energy,\" she commented, opening the clubroom door." 
    nvl clear
    stop music
    play sound "SE/dooropenslow.mp3"
    
    scene bg ClubroomBack
    show Yuki Chair1:
        xalign 0.8 yalign 1.0
    show MSew:
        xalign 1.15 yalign 0.6
    show ClubTable
    with slowflashbulb
    play music "Music/Nanika.mp3"
    "Yuki was in her normal seat, already halfway through a thick paperback titled, 'The Life of Pi'. Seated at the table near Yuki, Mikuru was tiredly resewing her maid costume. \"Oh? What happened to the costume, Mikuru-chan?\""
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
    show Haruhi Neutral4 at left_RightScreen
    show Mikuru Neutral1 at right_RightScreen
    show Kyon Neutral3 at center_RightScreen
    with dissolve
    $ renpy.layer_at_list([PanScene_LeftToRightSlow])
    nvl clear
    show Kyon Sigh2
    "\"Got a lot on {i}my{/i} mind,\" Kyon muttered, pulling his seat out and collapsing into it. \"Even if you don't. But, man am I {i}hungry{/i}.\""
    show Kyon Sigh4
    show Mikuru Smile3
    "\"It wasn't torn or anything,\" Mikuru answered, smiling. \"But this one seam scratched a tiny bit ... I realized how to restitch it to make it more comfortable.\""
    nvl clear
    show Mikuru Smile2
    show Haruhi Hap4
    "\"Well, I like that enthusiasm!\" Haruhi said, nodding her approval."
    show Haruhi Quest1
    "\"Hmm, I didn't know you knew a lot about sewing?\""
    nvl clear
    show Haruhi Quest2
    show Mikuru Sad2
    "For some reason, the older girl looked vaguely haunted. \"Yes, I know rather a lot about sewing,\" she mumbled, lowering her face and focusing on her needlework."
    show Mikuru Unhap1
    show Haruhi Hap1
    "\"Oh? Maybe I should get some supplies, and you can sew new costumes?\" Haruhi suggested."
    nvl clear
    show Haruhi Smile3
    show Mikuru Quest1
    "\"I don't know how to design costumes,\" Mikuru answered evenly. \"Maybe I will tomorrow. Otherwise, if you bring me a pattern and cloth, I'm sure I can make it.\""
    show Mikuru Neutral1
    show Haruhi Hap1
    "\"That's good ambition!\" she approved."
    show Haruhi Eyeroll1
    "\"Hey, Kyon, learn from her example, huh? Have a good reason to be tired. You were {i}totally{/i} dozing off during history. Luckily, I'm looking out for you, so I took some notes you can check out.\""
    nvl clear
    show Haruhi Eyeroll2
    show Kyon Sigh3
    "He blinked at her as she flourished the small stack of papers, taking them with a grave seated bow, made comical by the chopsticks he held in his mouth. \"Thanks,\" he managed around the utensils."
    show Kyon Worry1
    nvl clear
    show Haruhi Grin1
    "With obvious effort, he focused his eyes on the pages of notes she had taken, setting his chopsticks down. While he was distracted, she snagged his bento and the chopsticks, smirking as she finished the rest of it off. That'd teach him; next time he'd learn not to be so tired!"
    show Kyon Ser3
    nvl clear
    "He frowned at a particular line, turning his head sideways as he studied it. \"I don't think 'exactly like Genghis Kahn' tells me much,\" he said, glancing at her and then rolling his eyes when he saw his demolished lunch. \"Urg. Anyway, just saying something is like something else doesn't tell me anything when I don't remember the original reference.\""
    show Haruhi Ang2
    show Kyon Ser1
    nvl clear
    "\"You absolutely do,\" she challenged him. \"Didn't you say that I imposed order like Genghis Kahn, once?\""
    show Kyon Sigh2
    show Haruhi Ang5
    "\"What, wiping out all opposition in a bloody march with no quarter offered, replacing the older system with a regimented and cleanly run organization of your own devising?\" he asked, squinting. \"Something like that?\""
    nvl clear
    show Kyon Sigh4
    show Haruhi Hap4
    "\"Exactly like that!\" she replied, beaming. \"Man, you are so book dumb sometimes!\""
    show Haruhi Hap5
    show Kyon Puzzle1
    "\"I guess I did say that,\" he murmured, mildly disquieted. \"I must have perfected sleep-learning, or something.\""
    show Kyon Worry1
    nvl clear 
    show YBook at TopRight_RightScreen behind Mikuru with dissolve
    "\"You will improve with practice,\" Yuki remarked, flipping to the next page."
    hide YBook with dissolve
    show Kyon Neutral2
    "\"Anyway,\" he announced, rising to his feet, \"I'm still really hungry, so I think I'll see if there's anything left at the cafeteria.\""
    nvl clear
    play sound "SE/dooropenfast.wav"
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Kanae Hap2 at right
    show Koizumi Crossed Neutral1 at center
    "\"There isn't,\" Kanae answered him, opening the door and ducking her head slightly. Koizumi stood behind her with a large paper bag in both hands. \"I was really hungry after last night, too, but I guess I took too long to get there — I had to run off campus and stop by the bakery a block and a half away. Thankfully, Koizumi-san helped me out!\""
    nvl clear
    show Kanae Smile1
    "Kyon blinked, frowning as he glanced at the pair, then sighed and sank back into his chair. His stomach gave an unsettling growl, and Haruhi began to feel a little sorry that she'd taken half his lunch ... but then, the cafeteria was empty, and {i}she{/i} was still hungry, too."
    nvl clear
    show Koizumi Shrug Sigh1
    "\"I didn't expect a lunch meeting,\" Koizumi said cheerfully. \"But when I saw Michikyuu-san heading out of the campus, I thought I'd see if she needed help with anything.\""
    play sound "SE/doorclose.mp3"
    show Koizumi Think Smile2
    "Kanae pulled out a chair for herself and another for Koizumi as the esper closed the door behind him with one foot, then set the bag on the table. \"I hope no one has any problems with pork buns?\""
    show Koizumi Think Smile1
    show Kanae Hap4
    nvl clear
    "\"And chocolate cornets!\" Kanae added. {nw}"
    show Kanae Hap2
    show KABlush at right
    play music "Music/YareYare.mp3"
    extend "Blushing slightly, she handed one of the buns to Kyon, adding, \"Thanks for last night, Sempai.\""
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Haruhi Crossed Eyeroll1 at left_RightScreen
    show Kyon Neutral3 at center_RightScreen
    "Haruhi couldn't help when one of her eyebrows twitched. {nw}"
    show Haruhi Crossed Eyeroll2
    extend "\"Excuse me?\" she asked, distracted from the free food by that last comment."
    show Haruhi Crossed Eyeroll1
    $ renpy.layer_at_list([PanScene_RightToOffCenterL])
    show Kanae Hap4
    show Koizumi Think Sup1
    "\"It was the first time, I.... I mean....\" Kanae blushed more brightly. \"It wore me out quite a bit, but with Sempai and Nagato-san, I don't mind at all!\""
    nvl clear
    show Kanae Smile3
    show Haruhi Point Ang1 zorder 1
    play sound "SE/impact.mp3"
    $ renpy.layer_at_list([PanScene_OffCenterLToOffCenterR])
    "{=shout}\"Kyon!\"{/=shout} Haruhi screeched, standing up so quickly the chair beneath her rolled across the floor until it crashed into the wall behind her. {=loud}\"What is the meaning of this!?\"{/=loud}"
    show Haruhi Hips Ang4
    $ renpy.layer_at_list([PanScene_OffCenterRToRight])
    show Mikuru Sigh1
    "\"I'm pretty worn out from last night, too,\" Mikuru added, covering her mouth as she yawned."
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToOffCenterL])
    show Mikuru Sigh2
    show Koizumi Crossed Uneasy2
    "Koizumi winced, actually making a tiny whimper as he turned his gaze towards Kyon and begged, \"Please tell me that this is a misunderstanding?\""
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Ser3
    "\"I don't know what she's talking about,\" Kyon said defensively. \"I'm pretty sure I spent almost all last night learning martial arts.\""
    nvl clear
    show Kyon Ser1
    show Haruhi Ang4
    "{=loud}\"That's amazing, {i}Neo{/i}, now what does it have to do with you wearing out an underclassman!?\"{/=loud} Haruhi demanded, glowering down at him."
    show Haruhi Ang5
    show Kyon Neutral3
    "He stared up in befuddlement for a long moment before understanding dawned in his eyes."
    nvl clear
    show Kyon Sup1
    show Ksweat at center_RightScreen
    play sound "SE/impact.mp3"
    "{=shout}\"It is {i}not{/i} like that!\"{/=shout} he insisted, jumping to his feet and dismissing his exhaustion to protest hotly, his own chair sliding backwards into the clothing rack. {=loud}\"I swear to you — I did absolutely nothing inappropriate!\"{/=loud}"
    show Haruhi Eyeroll1
    "{=loud}\"Then what {i}happened{/i}?\"{/=loud} Haruhi growled, her eyes narrowing."
    show Kyon Worry3
    show Haruhi Eyeroll2
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToOffCenterR])
    show Kanae Hap3
    hide KABlush
    "\"Er, I said something wrong, maybe?\" Kanae said with an embarrassed chuckle, sticking her tongue out and miming a blow to her head. \"Last night I got to practice sliding! It took a long time, but I think I'm finally starting to learn how to control it a bit better, thanks to Sempai and Nagato-san! Asahina-san was there, too, but a lot of it gets really fuzzy....\""
    show Kanae Smile1
    show Haruhi Crossed Eyeroll2
    "\"T...that's all that it was, though?\" the brigade chief pressed, still glaring at Kyon."
    show Haruhi Crossed Eyeroll1
    nvl clear
    hide Ksweat
    show Kyon Puzzle1     
    "\"Er ... um ... Asahina-san, do you think you could help, here?\" he asked, turning a pleading gaze on the tired upperclassman."
    show Kyon Worry1
    $ renpy.layer_at_list([PanScene_OffCenterRToRight])
    show Mikuru Think Quest1
    "\"Kyon-kun was a good boy,\" Mikuru answered sleepily. \"It's Nagato-san's fault for teleporting me straight out of the shower.\""
    play sound "SE/DunDun.mp3"
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToOffCenterL])
    show Koizumi Crossed Sigh1
    "\"I...it seems that a rather large closed space has appeared,\" Koizumi said in a mournful tone. \"I'm afraid I will be absent for a while....\"" 
    show Koizumi Shrug Sigh1 at center
    "He bowed apologetically towards Haruhi, then nodded at Kyon, adding, \"I will leave everything else up to you.\""
    $ _window = True
    play sound "SE/dooropenfast.wav"
    #moveoutleft/right won't work properly on a two-screen scene such as this. 
    hide Koizumi with dissolve
    pause 0.5
    play sound "SE/doorclose.mp3"
    $ _window = False
    "As the esper marched out of the room, Kyon sighed and rubbed at his eyes, calling out, \"Good luck, Koizumi.\""
    show Kanae Neutral1 at center
    show Yuki Side1 at right
    with dissolve
    $ renpy.layer_at_list([PanScene_LeftToOffCenterR])
    nvl clear
    show Kyon Unhap1
    show Haruhi Crossed Tsun2
    "\"Yuki-chan,\" Haruhi said, before biting back her protest. {nw}"
    show Haruhi Crossed Tsun1
    extend "Well, she {i}had{/i} agreed that the other girl could 'borrow' Kyon. But what did she need with Mikuru and Kanae?!" 
    stop music fadeout 3
    show Haruhi Crossed Tsun2
    "\"I'm expecting an explanation for this!\" Come to think of it, what were the practical limitations of 'borrowing', anyway?"
    nvl clear
    play music "Music/Kokuhaku.mp3"
    show Haruhi Crossed Tsun1
    show Yuki Talk1
    show Kyon Neutral3
    "Yuki raised her gaze from her book languidly. \"Last night,\" she began, without preamble, \"I neared overload due to queued data-creation and modification requests from you." 
    show Yuki Talk2
    "\"To prevent overload, as per the instructions given by him and yourself, I undertook to dispose of all junk data and error-causing behaviors." 
    nvl clear
    show Yuki Talk1
    "\"After preparing all three subjects with nanites for preservation, Michikyuu Kanae attempted to slide to an alternate dimension, simultaneous to the activation of Asahina Mikuru's time travel device, while I engaged the dimensional anchor with a modified temporal anchor function."
    nvl clear
    show Yuki Talk2
    "\"The resultant actions, guided by stored data from yourself, were sufficient to create a semi-stable permeable reality governed by myself that was outside of both space and time, allowing me to ground myself from the negative attribute data that would cause error behavior."
    nvl clear
    show Yuki Talk1
    "\"This same space was also used to simultaneously allow Michikyuu Kanae practice sliding between nested pocket-dimensions and Asahina Mikuru to undertake her requested training in sewing. Per his own instructions, he undertook martial arts training and assisted me with ... personal issues.\""
    show Yuki Side Blink
    show Haruhi Crossed Worry2
    "Yuki blinked once as Haruhi absorbed everything."
    nvl clear
    show Yuki Talk2
    "\"After spending sufficient time to resolve internal issues, I restored all of us to the baseline physical reality and undid the time-based changes in physical age, as well as clearing out all non-necessary mental data to prevent unintentional corruption or trauma of hosts by acquired data.\""
    show Haruhi Crossed Worry1
    show Yuki Side2
    "\"You mean,\" Haruhi said, struggling, \"everyone spent last night training on stuff, and then you wiped it all out?\""
    nvl clear
    show Haruhi Crossed Worry2
    show Yuki Talk2
    "\"Negative. The results of training remain, even if the specific datum of acquisition are no longer present. Additionally, physical conditioning is preserved, even though aging was reversed. In this way, muscle memory and skill can be preserved memetically.\""
    $ renpy.layer_at_list([PanScene_OffCenterRToRight])
    nvl clear
    show Mikuru Think Quest1
    "\"How long did we actually spend there?\" Mikuru mused. \"It's strange, since I can ... kind of ... vaguely remember it, but not really {i}specifically{/i} recall much. Even so, I know much more about sewing, now.\" She gave a tiny shiver. \"{i}Much{/i} more. If I'd known, I'd have suggested something more serious....\""
    show Mikuru Neutral2
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToOffCenterR])
    show Yuki Talk1
    "\"One year of relative time was spent in training,\" Yuki answered."
    show Yuki Side1
    show Kyon Sigh1  
    "\"That'd explain it,\" Kyon said, shaking his head and settling back into his seat. \"I remember all of the basics of what I learned, and I felt strangely light this morning. And, weirdly enough, I felt like I really, really missed—\""
    show Kyon Worry1
    show KBlush at center_RightScreen
    "He coughed suddenly, staring into his half-eaten pork bun."
    nvl clear
    hide KBlush
    show Kyon Ser3
    "\"But, yeah. That's what happened. It's funny, though ... I know a full year of training in martial arts ... which is pretty much enough to realize I've got a long way to go.\" He sighed, shaking his head. \"Anyway, sorry about that, Haruhi. I guess it did sound a bit strange, the way Kanae-chan said it.\""
    $ renpy.layer_at_list([PanScene_OffCenterRToOffCenterL])
    show Kyon Ser1
    show Kanae Smile3
    show KABlush:
        xpos 0.435 yalign 1.0
    "\"Hehe.... My bad. Sorry, Sempai,\" Kanae added, still blushing as she half hid her face behind a pork bun."
    nvl clear
    show Haruhi Pout2
    "\"I'll say,\" Haruhi agreed, feeling oddly deflated. \"But, that's no fun! Why am I left out?\""
    show Haruhi Pout1
    show Yuki Talk2
    "\"Your presence would create more data,\" Yuki answered unapologetically. \"I would be more likely to enter an error state. This is undesirable.\""
    show Yuki Side2
    show Haruhi Pout2
    "\"Yeah, but I don't have to like it,\" Haruhi grumbled."
    show Haruhi Pout1
    $ renpy.layer_at_list([PanScene_OffCenterLToOffCenterR])
    nvl clear
    show Kyon Puzzle1
    "Kyon winced. \"You could try,\" he said, somewhat pleadingly. \"If not for us, then for Koizumi, who is working overtime for you, now.\""
    show Kyon Worry1
    $ renpy.layer_at_list([PanScene_OffCenterRToOffCenterL])
    show Kanae Worry1
    hide KABlush
    "\"Cornet?\" Kanae offered Haruhi sympathetically. {nw}"
    show Kanae Unhap2
    extend "\"Even though it felt like it was that long for us, Sempai still came back here with you the next day, right?\""
    nvl clear
    show Kanae Unhap3
    show Haruhi Crossed Tsun2
    "\"I guess,\" Haruhi agreed reluctantly, taking the pastry and biting the head end absently. \"But there better not be any fooling around in these dream-training things! And I don't care how busy you are, I'm {i}still{/i} making you pay attention in class, Kyon.\""
    show Haruhi Crossed Tsun1
    $ renpy.layer_at_list([PanScene_OffCenterLToOffCenterR])
    nvl clear
    show Kyon Sigh1
    "\"At least I've got that,\" he grumbled. \"Man, why am I so hungry?\""
    show Kyon Sigh3
    show Yuki Talk1
    "\"You will require more protein to generate the mass your conditioning has come to expect from your training,\" Yuki answered, turning her gaze back to her book."
    nvl clear
    show Kyon Sigh2
    show Yuki Side1
    "\"Yeah? I guess that makes sense. My own fault for asking for martial arts.\" Then he shook his head sharply, taking another bite from his pork bun before adding, \"Though it seems I'll need that to help Tsuruya-san a few days ago.\""
    nvl clear
    show Kyon Sigh4
    show Haruhi Crossed Sigh1
    "\"Huh? Yuki-chan, I would have expected you to take better care of him!\" Haruhi protested weakly, trying to remember that she needed to control her frustration."
    show Haruhi Crossed Sigh2
    show Yuki Talk2
    "Yuki looked up from her book, for a moment the merest hint of confusion flickering in her eyes. \"I thought you would wish to do that yourself,\" she said quietly."
    nvl clear
    show Yuki Side2
    show Kyon Neutral2
    "\"Delicious pork bun,\" Kyon mumbled, devouring another and studiously ignoring the conversation. \"Thanks again, Kanae-chan.\""
    show Kyon Neutral3
    show Haruhi Pout2
    show Hblush at left_RightScreen
    "Haruhi felt her face color as she nodded. \"Right,\" she decided. \"Come on, Kyon, grab another bun and let's get back to class before the bell, okay?\""
    nvl clear
    scene bg hallway with fade
    show Kyon Smile6 at right
    show Haruhi Pout1 at TenthLeft
    show Hblush at TenthLeft
    with dissolve
    "\"Sure,\" he agreed, taking the notes she had made for him and following her out of the clubroom. \"And, thanks for the help with my schoolwork.\""
    show Kyon Smile1
    show Haruhi Pout2
    "\"No problem,\" she mumbled while they walked down the stairs. \"It's not as neat as training you in martial arts in your sleep, though.\""
    nvl clear
    show Haruhi Pout1
    show Kyon Smile7
    "\"It's something I can talk to my parents about without being sent to an institution,\" he told her, smirking. \"Isn't that something?\""
    show Kyon Smile2
    show Haruhi Quest1
    "\"What's with you trying to be so nice?\""
    nvl clear
    show Haruhi Quest2
    show Kyon Sigh2
    "\"It's no good seeing you when you're feeling down,\" he said, shrugging apologetically. \"Didn't I already tell you that?\""
    show Kyon Sigh4
    show Haruhi Smile1
    "\"Hmm,\" she mused, giving a weak smile. {nw}"
    show Haruhi Neutral3
    extend "\"Well, that's something.\""
    show Haruhi Smile1
    nvl clear
    stop music fadeout 3
        
    call eyecatch_fancy("Tuesday, April 19") from SF2_sc002

    play music "Music/worldendsolo.ogg"
    scene bg classroom:
        size (800,600)
    show Kyon Sigh2 at right
    with fade
    "After class finished, Kyon cracked his neck, unconsciously stretching his muscles and joints while switching stance from foot to foot, as though in preparation for a fight. Suddenly knowing basic martial arts was strange, if very convenient from a practical standpoint. Knuckling back another yawn, he turned around to follow Haruhi to the clubroom, surprised to see her ordering a stack of note paper, still sitting at her desk."
    nvl clear
    show Kyon Sigh4
    show Haruhi Pout2 at TenthLeft with dissolve
    show Hblush at TenthLeft
    "\"Here,\" she said, thrusting the papers towards him without meeting his eyes. \"You're exempted from the club meeting today. Go home and get some rest. If you're not too tired tomorrow morning, we'll go over the homework before class.\""
    show Haruhi Pout1
    show Kyon Puzzle1
    nvl clear
    "\"...thanks,\" he managed, frowning. \"Um, Haruhi, are you upset with me?\""
    show Kyon Worry1
    show Haruhi Pout2
    "\"Not with you,\" she said, grimacing. \"Anyway, I need to have a talk with Yuki-chan and Mikuru-chan.\""
    show Haruhi Pout1
    show Kyon Ser3
    "He blinked away some of his exhaustion. \"If there's anything I can help you with—\""
    show Kyon Ser1
    hide Hblush
    show Haruhi Sigh1
    nvl clear
    "\"This is something I have to figure out for myself,\" she said, shaking her head. \"Really, just get some rest. We're going to have a lot to talk about tomorrow.\""
    show Haruhi Sigh3
    show Kyon Puzzle1
    "\"Okay,\" he allowed, wishing that either of them were smiling at the moment. \"Well ... take care, then.\""
    show Kyon Worry1
    $ _window = True
    hide Haruhi with moveoutright
    $ _window = False
    "She nodded before breezing out of the classroom."
    nvl clear
    show Kyon Neutral3 at right
    $ _window = True
    show Taniguchi Smile1 at left behind Kyon with dissolve
    $ _window = False
    "\"Trouble in paradise?\" Taniguchi mused, drawing close."
    show Taniguchi Grin1
    $ _window = True
    show Kunikida Ser2 at center behind Kyon, Taniguchi with dissolve 
    $ _window = False
    "\"And what's this about you fighting thugs for Tsuruya-sempai?\" Kunikida asked, following with a concerned expression."
    show Kunikida Ser1
    show Taniguchi Ser1
    nvl clear
    "\"Yeah,\" Taniguchi said, nodding seriously. \"Suzumiya talking about nonsense like time traveling isn't going to raise too many questions, but people attacking a sempai, and you getting into fights?\""
    nvl clear
    show Taniguchi Ser3
    "\"I hate to tell you that you should back off, since you and Suzumiya seem to be heading toward 'item' territory ... but if she's losing it, I don't think you want to get dragged down with her.\""
    show Taniguchi Ser2
    show Kyon Sigh1
    nvl clear
    "Kyon looked down to the stack of note papers in his hand. \"Thank you, Taniguchi,\" he said, struggling for an earnest tone. \"I should be honored to have a friend like you, trying to spare me the indignity of being dragged into a whirlpool of depravity and academic success.\""
    nvl clear
    show Kyon Sigh3
    show Kunikida Ser2
    "Kunikida chuckled weakly. \"To be fair, Kyon,\" he said, shifting his shoulders uncomfortably, \"even if it wasn't worded diplomatically.... Well, perhaps it would be better to say that you're generally a respectable person. If you're, ah, pursuing companionship solely for help in studying, wouldn't Sasaki-san be a better choice?\""
    nvl clear
    show Kyon Sigh3
    show Kunikida Ser1
    "Struggling to think of an acceptable response, Kyon frowned and cracked the knuckles on both hands, {nw}"
    show Taniguchi Ser2:
        linear 0.3 xpos -0.05
    show Kunikida Ser1:
        linear 0.3 xpos 0.45
    extend "prompting his friends each to take a step back."
    show Kyon Ser3
    "\"What, precisely,\" he asked, \"has changed? Haruhi hasn't become somehow worse, or really that different than she was last year.\""
    nvl clear
    show Taniguchi Ser1 at left with move
    show Kyon Ser1
    "\"Yeah, well ... she's rubbing off on you,\" Taniguchi said, spreading his arms in a helpless gesture. \"It was great when you somehow were taming the shrew. Don't get me wrong, it was nothing short of a miracle that you were able to reach her! But now she's turning you a bit crazy.\""
    nvl clear
    show Taniguchi Ser2
    show Kyon Sigh2
    "\"I'm not sure what's gotten into you two,\" Kyon decided. \"But I haven't been resting well lately. Maybe I seem more docile because I'm tired, but you're probably making too much of it. What does a joke between Haruhi and myself have to do with the rest of us going about our business as normal?\""
    nvl clear
    show Taniguchi Sigh1
    show Kyon Sigh4
    "\"Well, if it was just Haruhi, that'd be fine,\" Taniguchi said, shaking his head. \"But Tsuruya-sempai mentioned you getting into a fight on her behalf, as well. She's too well respected to be considered responsible for it, and she's not the type to spread baseless rumors, so naturally....\""
    nvl clear
    show Taniguchi Sigh2
    show Kunikida Ser2 at center with move
    "\"It's just that the general consensus is, grades aside ... if you're getting into trouble, Haruhi must be behind it,\" Kunikida finished. \"Especially since she mentioned it earlier ... that pretty much seemed to confirm that it wasn't a joke. You don't want a reputation as a delinquent, do you?\""
    nvl clear
    show Kunikida Ser1
    show Kyon Puzzle1
    "\"Tsuruya-sempai thinks I'm a delinquent?\" Kyon asked skeptically."
    show Taniguchi Ser1
    show Kyon Neutral3
    "\"Well, no, she said you were a warrior-philosopher, or something else silly like that,\" Taniguchi said, shaking his head and making a dismissive gesture with one hand. \"But what else do you call someone who solves problems with violence?\""
    nvl clear
    show Taniguchi Ser2
    show Kyon Ser2
    "\"A problem solver?\" Kyon asked. \"Anyway, I don't know what else to say, here. I appreciate the warning, I guess, but if it comes down to it, I'm at Haruhi's side until the end — so, sorry.\"" 
    nvl clear
    show Kyon Sigh2
    "When Taniguchi opened his mouth to say something else, Kyon raised a hand to forestall further comment. \"I'm really tired. I'm going home to get some rest. Maybe this whole thing is a product of inadequate sleep, and we'll all feel better about it tomorrow.\""
    nvl clear
    show Kunikida Neutral2
    show Kyon Sigh4
    "\"That seems very peaceable,\" Kunikida agreed, shooting Taniguchi a warning look as Kyon's hand dropped to his side."
    show Taniguchi Sigh1
    show Kunikida Neutral1
    "Unsatisfied with silence, Taniguchi said, \"Well, be careful at least.\""
    show Taniguchi Sigh2
    nvl clear
    stop music fadeout 3

    call eyecatch_fancy("Tuesday, April 19") from SF2_sc003

    play music "Music/HizundaKokoro.mp3"
    scene bg ClubroomBack
    show Yuki Chair1 at right
    show ClubTable
    with fade
    "Haruhi reached the clubroom second, Yuki somehow being there first, as she usually was."
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
    show Haruhi Quest1 at left
    show Yuki Right Neutral1 at right
    with dissolve
    "\"Not visiting the computer research society much these days?\" she asked the slighter girl, who had almost finished her paperback."
    show Haruhi Quest2
    show Yuki Right Neutral2
    "Yuki blinked slowly, then gave a minuscule shake of her head."
    nvl clear
    show Haruhi Neutral2
    "\"Yuki-chan, we need to talk about Kyon.\""
    show Haruhi Neutral1
    show Yuki Right Neutral2
    "The smaller girl gave a tiny nod and closed her book, turning to look at Haruhi expectantly."
    show Haruhi Crossed Tsun1
    "For her part, the brigade leader walked to her desk, turning the computer on to give herself a brief distraction."
    nvl clear
    show Haruhi Crossed Tsun2
    show Hblush Crossed at left
    "\"You like Kyon, don't you?\" she finally blurted out."
    show Haruhi Crossed Tsun1
    show Yuki Right Talk1
    "\"Yes,\" Yuki answered softly, her eyes still fixed on Haruhi."
    nvl clear
    show Yuki Right Neutral1
    show Haruhi Pout2
    hide Hblush
    "\"Um, anyway, Yuki-chan ... I {i}did{/i} say you could borrow him when you needed to,\" Haruhi admitted, frowning. \"But I'm having a hard time figuring things out right now.\""
    show Haruhi Pout1
    show Yuki Right Neutral2
    "Yuki said nothing, merely staring in silence."
    nvl clear
    show Hblush at left
    show Haruhi Pout2
    "\"I.... I mean, Kyon and I....\" She hesitated, uncertain what to say. Eventually, in a very quiet voice, she managed to ask, \"Are you going to start dating Kyon?\""
    show Haruhi Pout1
    show Yuki Right Talk1
    "After blinking once, Yuki answered, \"I do not seek to initiate courtship rituals or physical intimacy with him, though I will reciprocate if he demonstrates an obvious inclination."
    nvl clear
    show Yuki Right Talk2
    "\"However, as has been observed previously, my understanding of his genuine desires and emotions is faulty; I can therefore not safely assume that such demonstrations have occurred without verifying them through a third party.\""
    show Yuki Right Neutral2 
    show Haruhi Eyeroll1
    hide Hblush
    "Haruhi stared at the smaller girl hard, furrowing her brow. \"You're telling me,\" she said slowly, \"that you can't tell if Kyon likes you, and you don't want to mess things up? So you'd need to ask someone else if he really liked you and wanted to date?\""
    show Haruhi Eyeroll2
    show Yuki Right Neutral1
    nvl clear
    "Yuki's face tilted upwards slightly, as though she were considering the statement." 
    show Yuki Right Talk1
    "\"Yes,\" she answered after an extended pause. \"That third party must be trusted; I would like to nominate you.\""
    show Haruhi Pout1
    show Yuki Right Neutral2
    nvl clear
    "Drumming her fingers on the desk, glancing at the monitor as the OS screen flashed past and the generic blue background appeared, Haruhi asked, {nw}"
    show Haruhi Pout2
    extend "\"You want me to help you hook up with him?\""
    nvl clear
    show Haruhi Pout1
    show Yuki Right Talk2
    "The smaller girl's gaze lowered. \"Uncertain,\" she answered. \"Our behaviors do not conform to typical models among humans. I am unable to determine how this would change the interactions between the group definitively, but there is a significant probability that committing to such a course of action would result in dissatisfaction among most others.\""
    nvl clear
    show Haruhi Sigh1
    show Yuki Right Neutral2
    "\"Yeah,\" Haruhi sighed, rubbing at her temples. \"If only there was a way for everyone to be happy, huh? But there's only one Kyon to go around....\""
    show Haruhi Hap1
    "She brightened suddenly. \"Ooh! Hey, Yuki-chan, what about, um, making a bunch of copies of Kyon!\""
    nvl clear
    show Haruhi Smile3
    show Yuki Right Neutral1
    "She stared at Haruhi blankly for a minute, then pointedly turned her attention back to the book in her hands."
    $ _window = True
    hide Yuki with dissolve
    $ _window = False
    show Haruhi Sigh2
    "\"Yeah, you're right,\" Haruhi grumbled with another resigned sigh. \"Don't even let Kyon know I suggested that; he wouldn't like it.... Maybe I should just resign myself to letting him choose whoever he wants ... I mean....\"" 
    nvl clear
    show Haruhi Pout1
    "She trailed off, staring at the ceiling and musing absently until she was distracted by Kanae and Mikuru walking into the room."
    nvl clear
    play sound "SE/dooropenfast.wav"
    $ _window = True
    show Mikuru Sigh2 at right
    show Kanae Neutral1 at center
    with moveinleft
    $ _window = False
    show Mikuru Sigh1
    "\"Hello Suzumiya-san,\" Mikuru said sleepily, collecting her sewing kit and the maid costume from where it had been left to finish her repairs."
    show Mikuru Sigh2
    show Haruhi Neutral2
    "\"Hey, Mikuru-chan, Kanae-chan.\""
    show Haruhi Neutral1
    show Kanae Quest1
    "\"Hi, everyone,\" the younger girl mumbled. \"Oh, no Sempai...?\""
    show Kanae Quest2
    show Haruhi Sigh2
    nvl clear
    "\"Close the door, Kanae-chan,\" Haruhi instructed. \"Lock it, too. Koizumi's ... working because I'm problematic, and I sent Kyon home to get some sleep.\""
    play sound "SE/doorclose2.mp3"
    show Haruhi Unhap3
    show Mikuru Think Quest2
    show Kanae Neutral1
    "\"Um?\" Mikuru noised, as Kanae followed her orders and took Koizumi's normal seat at the table. \"I...is something wrong? Suzumiya-san, if you and Kyon-kun aren't getting along—\""
    show Mikuru Think Quest3
    show Haruhi Neutral2
    nvl clear
    "\"It's nothing to do with him and I,\" she said crossly, rubbing at her forehead and spinning her chair to face the window, adjusting herself to sit cross-legged on the seat. \"Because, Mikuru-chan ... you like Kyon, don't you?\""
    show Haruhi Neutral1
    show Mikuru Cower Smile1
    "Mikuru yelped quietly, looking up in alarm and sucking the fingertip she had pricked with her sewing needle. \"Er.... That is.... Of course! He's a very good friend!\""
    nvl clear
    show Mikuru Cower Nervous1
    show Haruhi Eyeroll1
    "\"You don't have to act clueless and moe right now,\" Haruhi grumped. \"I mean, romantically. If I weren't being an obstacle to you, you'd try and date him, wouldn't you?\""
    show Haruhi Eyeroll2
    show Mikuru Cower Nervous3
    show Kanae Worry1
    "\"Er.... Uh....\""
    show Haruhi Ang4
    "\"Be honest!\""
    show Haruhi Ang5
    show Mikuru Sad2
    nvl clear
    "\"It's ... forbidden,\" Mikuru said quietly. \"I...if you must know, then ... yes, I do like Kyon-kun ... he's reliable, and doesn't have ulterior motives." 
    nvl clear
    show Mikuru Sad1
    "\"But I'm not {i}from{/i} this timeplane; I can't have, um, relationships with anyone from here. S...so, please don't think of me as a threat, Suzumiya-san! And you can't ask me to think of him without you being in the picture; if it weren't for {i}you{/i}, I never would have been sent back and been able to meet him anyway! I don't want to come between the two of you!\""
    nvl clear
    show Haruhi Unhap2
    show Mikuru Unhap2
    "Haruhi stuck one foot out and turned the chair around to face her club members. Kanae rubbed at one eye and peered at Mikuru in bemused fascination, while Yuki's eyes were fixed firmly on Haruhi. Mikuru herself merely gazed at her sewing project with a bowed head, her hands not moving, her expression downcast."
    show Mikuru Sad2
    nvl clear
    "\"I'm not a threat to you,\" Mikuru repeated quietly. \"I never could be.\""
    show Haruhi Pout2
    show Mikuru Unhap1
    "\"I don't like that answer,\" Haruhi mumbled. \"It's just like an action movie where the hero dies. Or where the hero likes two girls, so one isn't quite as pure-hearted or kind as the other, and is killed to make it so the hero never has to choose. Yuki-chan likes Kyon, too. {nw}"
    show Haruhi Sigh2
    extend "Augh! This is frustrating, really, really frustrating!\""
    show Haruhi Unhap3
    show Mikuru Sad1
    nvl clear
    "\"P...please don't get frustrated!\" Mikuru begged. \"There's nothing to worry about from me! Kyon-kun and I ... will never be more than friends.\""
    show Haruhi Sigh1
    show Mikuru Unhap2
    "Haruhi sighed, pushing the keyboard away from her so she could cross her arms and rest her head there. \"Maybe I'm thinking about things too hard,\" she forced out. \"Maybe, really, I should be asking who {i}he{/i} likes, right?\""
    show Haruhi Sigh3
    show Kanae Unhap2
    nvl clear
    "\"This got really serious,\" Kanae said, shivering. \"Um, what's going on?\""
    show Kanae Unhap3
    show Haruhi Pout2
    show Hblush at left
    "\"I'm trying to sort things out,\" Haruhi answered. \"Kyon didn't mention it ... but for a while I thought maybe he liked me ... then I thought about it more and realized, maybe he's just being so nice to me because he {i}has{/i} to be.\""
    nvl clear
    show Haruhi Pout1
    show Kanae Sup2
    "\"That's not true at all!\" Kanae said firmly, shaking her head. \"I've been to a lot of worlds, and in some of them you have a power, and in some you don't. But Sempai likes you in a {i}lot{/i} of them. That can't be just coincidence.\""
    show Haruhi Quest1
    show Kanae Unhap3
    "\"He does?\" Haruhi asked hopefully, turning her eyes to the underclassman. \"It wouldn't be so much of a problem if he would just admit it and make the first move!\""
    nvl clear
    show Haruhi Quest2
    show Kanae Hap4
    "Kanae nodded quickly. \"Absolutely,\" she said cheerfully. \"It makes me a bit jealous; most worlds I jump to, he wants to help me but has to take care of you, more....\"" 
    show Kanae Sad5
    "She shrugged, her smile slipping momentarily before she forced more cheer. {nw}"
    show Kanae Hap3
    extend "\"But ... that's what's great about Sempai! He doesn't have to want to ask me out to care about me and want to make sure I'm okay. And that's ... fine ... for me.\""
    show Kanae Smile1
    show Haruhi Eyeroll1
    hide Hblush
    nvl clear
    "Haruhi drummed her fingertips on her desk absently. \"You really think so?\" she asked quietly, wondering about Kanae's actual feelings. Fleeing constantly through alternate realities, with Kyon as the only reliable person she knew.... That situation seemed oddly familiar."
    nvl clear
    show Haruhi Eyeroll2
    show Mikuru Ser2
    "\"I think so,\" Mikuru said earnestly. \"Don't let yourself get down, Suzumiya-san! If Kyon-kun ... didn't like you, he wouldn't have tried so hard when he asked you to help Nagato-san. He would have found a way to break things off with you at the same time, or give up your powers for good! He didn't, so....\""
    nvl clear
    show Haruhi Pout2
    show Mikuru Ser3
    "Haruhi's fingers drummed the table again. \"I still don't like that answer,\" she mumbled."
    show Haruhi Pout1
    nvl clear
    stop music fadeout 3
    
    call eyecatch_fancy("Tuesday, April 19") from SF2_sc004

    play music "Music/KyoufunohajimariStart.mp3"    
    scene bg SchoolEntranceLeft
    show Kyon Neutral3 at right
    show Mori Neutral1 Flip at left
    with fade
    "In a dark mood, Kyon strode out of the school grounds. He paused a few steps out of the gate as a mature woman in a sharp suit approached him, giving a terse nod."
    show Kyon Neutral2
    "\"Mori-san,\" he greeted her neutrally, struggling to keep the irritation his classmates had instilled from his face."
    show Kyon Neutral3
    show Mori Nervous1 Flip
    "\"Sir,\" she greeted him, somewhat stiffly. \"I'm here for our meeting, as you requested?\""
    nvl clear
    show Kyon Sigh1
    "He took a deep breath and gave the woman a slow nod of his own. \"Is Koizumi in trouble?\" he asked."
    show Kyon Sigh3
    show Mori Neutral2 Flip
    "Her expression eased slightly as she shook her head. \"He's just busy at the moment, Sir.\" He spent an idle moment wondering what the hell his future self was going to say to this woman that had made her so deferential to him. \"This way...?\""
    show Mori Neutral1 Flip
    nvl clear
    "The familiar black cab awaited a short distance down the street, and he shrugged at it in bemusement. It would get him home faster, letting him bypass the train. Which in turn, most likely meant that he {i}should{/i} get more sleep once he got home...." 
    nvl clear
    scene bg Cab with fade
    play sfxloop "SE/CarBackgroundLong.mp3"
    show Kyon Neutral3 at right
    show Mori Neutral1 Flip at left
    with dissolve
    "He got into the back seat, Mori opening the door on the opposite side and sitting next to him. Arakawa wordlessly started the car up."
    show Kyon Neutral2
    "He didn't feel like trying to puzzle through whatever it was that his future self had arranged, so he decided he'd try relying on raw bluster: \"If you'd care to begin...?\""
    nvl clear
    show Mori Neutral2 Flip
    show Kyon Neutral3
    "\"Very well,\" she agreed. \"While en route to his current assignment, Koizumi-kun relayed an update on the situation with Suzumiya-san.\""
    show Mori Neutral1 Flip
    show Kyon Neutral2
    "\"Okay. And...?\""
    nvl clear
    show Mori Neutral2 Flip
    show Kyon Neutral3
    "\"So far,\" Mori said evenly, her eyes turning to fix on some distant point outside of the car window, \"everything regarding Suzumiya-san has matched your predictions. Assuming you're correct, and tomorrow morning is the peak of closed space creation for the two week period that we established, then we'll accept that you have the situation under control.\"" 
    show Mori Ser1 Flip
    nvl clear
    "Her eyes hardened and shifted to his; he felt he should be trying to return her hard stare, but could only gaze back lethargically. Hopefully, he told himself, the lack of excited reaction would convey some sense of confidence to her." 
    nvl clear
    show Mori Nervous1 Flip
    "Surprisingly enough, it seemed to, and she quickly looked away again. \"In the meantime,\" she continued, unprompted, \"we're also following up on your request to ensure that Michikyuu Kanae is provided the same protection you are afforded. Naturally, since she's joined Suzumiya-san's club, this makes her a person of interest to us anyway.\""
    show Kyon Neutral2
    nvl clear
    "\"Of course,\" he said, nodding. Why had he thought to request that from Arakawa? It made sense the Organization would watch over anyone in the Brigade {i}anyway{/i}, if only to determine who they were and what powers, if any, they might have. Stabbing blindly at the next conversation topic, he asked, \"And the puppet Student Council?\""
    nvl clear
    show Mori Neutral3 Flip
    show Kyon Neutral3
    "\"Well, as you said, Sir,\" Mori sighed, \"there's not much we can do about Kimidori Emiri. However, she was never part of our equations anyway; in fact, we typically tried to hide our agenda from her because the IDSE and ourselves have our own goals. If she's an enemy, I don't hesitate to lay that problem firmly at {i}your{/i} feet, since you've started this mess. That being said, we had nothing planned within the next two weeks anyway.\""
    show Mori Neutral1 Flip
    show Kyon Sigh2
    nvl clear
    "\"Right,\" he said, committing the details to memory. This would absolutely have to be written down if he was to manage whatever madness he was going to do last Sunday." 
    nvl clear
    show Kyon Neutral2
    "\"Good. Did Koizumi mention the potential IDSE bargaining chip we had on the table?\" Those words sounded good ... right out of an intrigue filled political drama. Doubtless Haruhi would be thrilled to hear this story later."
    show Mori Neutral4 Flip
    show Kyon Neutral3
    "\"New data?\" Mori asked, giving a small nod. \"Again, that falls firmly into the area of 'not our problem'.\""
    show Kyon Ser3
    nvl clear
    "\"I know,\" he said patiently. \"But if we're working together, well, as I mentioned before, I'd like us to be on friendly terms. My plan isn't something inane, like, 'bite off more than you can chew and chew it anyway'. While I am doing my best, I don't have the arrogance to believe I'm infallible.\""
    nvl clear
    show Mori Grin1 Flip
    show Kyon Ser1
    "Mori turned her face back to him, her eyes softening as she raised her eyebrows. \"More and more, I'm starting to like you, Sir,\" she said with a wry grin." 
    nvl clear
    show Mori Ser1 Flip
    "\"You remind me of myself at your age. Well, in that case, the only thing that occurred to me is that ... this entire thing, every action you've taken so far, could be an IDSE orchestrated ploy. That is to say ... for all we know, they've arranged things from behind the scenes specifically so that you would 'collar' Suzumiya-san and thus restrict their precious 'data creation' to a safely controlled vector.\""
    show Kyon Neutral3
    nvl clear
    "The thought chilled him deeply, to consider he could have been manipulated so perfectly. If it were true, had Yuki betrayed him? Or was she, too, just a puppet? He didn't like the idea of anyone being a puppet for anyone else.... Resolving to ensure that Haruhi endured less harsh restrictions from himself in the future, he gave a thoughtful nod he didn't quite feel."
    nvl clear
    show Kyon Neutral2
    "\"Then again,\" he said, realizing that thanks to exhaustion, his expression hadn't changed despite his alarm, \"this also connects to the other theories of the Organization; Haruhi is God, for example.\"" 
    nvl clear
    show Kyon Neutral3
    "He'd never believed that one.... Able to warp reality, sure, but God? Even Koizumi said he hadn't bought into that one, and he was the closest thing to a Haruhi-worshiper Kyon had ever met. {nw}"
    show Kyon Neutral2
    extend "\"I don't think I'm going to ask Haruhi to create a rock she can't move anytime soon ... but we can't exactly prove this, can we?\""
    show Kyon Neutral3
    show Mori Neutral2 Flip
    nvl clear
    "\"We can't,\" Mori agreed. \"I'm guessing you had already considered it, then?\""
    show Mori Neutral1 Flip
    show Kyon Sigh2
    "\"Not really,\" he admitted. \"The theory's sound, but I don't believe any of us are predictable enough for the IDSE to risk it. I can easily see them wanting Haruhi controlled to provoke reactions safely, but threatening Yuki? After what I told them?\""
    nvl clear
    show Kyon Smile7
    "\"That's like giving a monkey a chainsaw and hoping that it'll create a new form of art. It might work, but probably it's just going to get messy and end poorly.\""
    show Kyon Smile2
    show Mori Smile1 Flip
    "Eyes widening in surprise, Mori laughed aloud; from the front seat, even Arakawa snickered. \"Your argument is as compelling as mine,\" Mori allowed, recovering."
    nvl clear
    show Mori Smile3 Flip
    "\"Neither can truly be proven yet. Very well, Sir. I hope for all of our sakes, you're able to do as well as you claim. {nw}"
    show Mori Neutral2 Flip
    extend "In the meantime, is there anything else your plans will require?\""
    show Mori Neutral1 Flip
    show Kyon Neutral2
    "\"Nothing serious, for the moment,\" he said dismissively. \"Maybe a coffee machine for the club room, at the rate things are going.\""
    nvl clear
    show Kyon Neutral3
    show Mori Smile1 Flip
    "\"If everything works out after tomorrow, it will be a small price to pay, Sir,\" Mori agreed as the car pulled to a stop. \"Koizumi-kun has made that request many times. Thank you again for your candor, and good luck with your objectives.\""
    nvl clear
    stop sfxloop
    scene bg KyonHouseDay with wipeup
    show Kyon Smile6 at right
    with dissolve
    "\"Don't mention it, Mori-san,\" he replied, somewhat bemused as he opened the door and stepped out of the car, waving at the pair as the vehicle drove away. {nw}"
    show Kyon Smile4
    extend "Did the clubroom actually have a coffee machine coming to it...? That would be amusing ... but he'd feel guilty if it got back to Haruhi as any kind of abuse of his authority."
    nvl clear
    show Nonoko Smile1 at TenthLeft
    with dissolve
    show Kyon Worry1
    "He saw his sister approaching, looking over her shoulder at the vanishing car curiously. {nw}"
    show Kyon Puzzle1
    extend "\"I even said I wasn't serious,\" he mumbled to himself. \"Well, it's not like everything I say I want will come to me. If it were, I'd wish that Haruhi and I could really get along, and she'd find a way to be happy.\""
    show Kyon Worry1
    show Nonoko Quest1
    nvl clear
    "\"Haru-nee-san isn't happy?\" his little sister asked, drawing close enough only to hear the last part."
    show Kyon Sigh2
    "\"Oh, you know,\" he said with a yawn. \"She wants me to study harder.\""
    nvl clear
    show Nonoko Hap1
    show Kyon Sigh4
    "\"So does Mom!\" his sister said brightly. \"She's always telling me to study harder than you, since you set the bar low!\""
    $ _window = True
    show Nonoko Smile1
    hide Kyon with dissolve
    "\"That's swell,\" he grumbled, rolling his eyes and heading into the house. \"Here's an easy bar to clear: I'm going to take a nap.\""
    nvl clear
    show Nonoko Quest1
    "\"What does setting a bar mean?\""
    show Nonoko Smile1
    nvl clear
    stop music fadeout 3
    
    call eyecatch_fancy("Tuesday, April 19") from SF2_sc005

    
    play music "Music/circulation.ogg"
    scene bg YukiRoomCenter
    show Yuki Side1 at left
    show Kyon Sigh3 at right
    with fade
    "His eyes slowly blinked open from his nap, staring upward into Yuki's eyes as she peered down at him. He forced back\na yawn and sat up, glancing around her apartment. "
    show Mikuru Cower Towel Unhap1 behind Kyon:
        xalign 0.7 yalign 1.2
    show Kanae Night Smile1:
        xalign 0.3 yalign 1.2
    with dissolve
    extend "Looking somewhat irritable and wearing a bathrobe, Mikuru knelt at the table, mumbling about getting phone calls first. Kanae was sitting next to Mikuru, working on her homework and evidently unperturbed."
    nvl clear
    show Kyon Sigh2
    "\"Hello?\" he said by way of greeting, looking down at himself ... he was wearing his dress shirt and slacks, too tired to change into his pajamas or strip. Though, that last thought was thankful, in retrospect."
    nvl clear
    show Kyon Sigh3
    show Kanae Night Sup1
    "Kanae blinked at his voice and looked around. \"Oh!\" she exclaimed. \"This isn't my room! I didn't even feel the slide!\""
    show Mikuru Cower Towel Nervous3
    show Kanae Night Quest1
    "\"I did,\" Mikuru said with a sigh. \"Nagato-san, are you trying to embarrass me?\""
    show Mikuru Cower Towel Nervous1
    show Kanae Night Quest2
    show Yuki Talk1
    "Yuki turned her gaze to Mikuru without changing expression. \"No,\" she answered. \"With your permission, we shall proceed again.\""
    nvl clear
    show Yuki Side1
    show Kyon Neutral2
    "Shifting his shoulders, Kyon sat up and nodded. \"Is this going to be a nightly occurrence?\" he asked, trying to keep annoyance from entering his voice."
    show Kyon Neutral3
    show Yuki Talk2
    "\"Unknown,\" Yuki answered. \"The amount of time Michikyuu Kanae will require to master her ability to shift dimensions is as of yet undetermined.\""
    nvl clear
    show Yuki Side2
    show Kyon Neutral1
    "\"Oh, right,\" Kyon realized, blinking. This wasn't {i}just{/i} about Yuki dealing with her 'error' data. \"Well, in that case, I'm ready, Nagato. I think I've got a way to go before I finish what I chose to learn ... and I can't travel back to last Sunday until I finish it.\""
    show Kyon Neutral3
    show Kanae Night Hap1
    "\"More sliding practice!\" Kanae cheered, throwing her hands into the air excitedly. \"I've never been so fortunate in any world I've jumped to!\""
    nvl clear
    show Kanae Night Smile1
    show Mikuru Cower Towel Smile2
    "\"Um, I should keep a positive attitude, too,\" Mikuru contributed. \"If it's not too much trouble, Nagato-san, could you call me before teleporting me here next time? I'd really like to arrive dressed ... if Suzumiya-san were to hear about, um, me arriving in such a condition on a regular basis, she'd probably become even more upset.\""
    nvl clear
    show Mikuru Cower Towel Worry1
    show Kyon Ser3
    "\"She's upset right now?\" Kyon asked, frowning. \"That's no good; what's wrong?\""
    show Yuki SideDisappointed1
    show Kyon Ser1
    "Yuki looked away, adopting an expression Kyon hadn't seen since he asked her what happened to people after they died. "
    show Yuki SideDisappointedTalk1
    extend "\"I should not say,\" she eventually answered."
    nvl clear
    show Yuki SideDisappointed1
    show Kyon Puzzle1
    "\"Well,\" he said, frowning, \"I already {i}know{/i} that there's supposed to be a huge closed space incident tomorrow. Do you have any advice on that front?\""
    show Yuki Talk2
    show Kyon Worry1
    "Her eyes ponderously swung back to meet his. \"Seek happiness.\""
    nvl clear
    show Yuki Side2
    show Mikuru Cower Towel Smile2
    show MBlush Cower Towel:
        xalign 0.7 yalign 1.2
    "\"Er, um,\" Mikuru managed, her face turning red, \"you should ... make the first move. Suzumiya-san is just ... stressed that.... Well, I probably shouldn't say, either. But I trust you to sort things out!\""
    show Kanae Night Hap1
    show Mikuru Cower Towel Worry1
    "\"Go Sempai!\" Kanae cheered again. \"I'm confident he can do it!\""
    nvl clear
    show Kanae Night Smile1
    show Yuki Talk1
    "\"If you are ready to proceed?\" Yuki asked, turning her gaze to Kyon again."
    show Yuki Side1
    show Kyon Neutral2
    "\"Yeah,\" he agreed. \"No need to put off your error correction any further than required.\""
    nvl clear
    show Yuki Talk1
    show Kyon Neutral3
    "\"Understood. Initializing,\" Yuki announced, and for a moment, Kyon wondered how Kanae could not have noticed being teleported as the world exploded away around him."
    nvl clear
    play sound "SE/ShieldLaunch.wav"
    scene bg Space:
        xpos 0 ypos 0
    with circleirisoutfast
    scene black with fade
    "Again."
    nvl clear

    jump SF3
