#Chapter 6, Heroic Antics Begin Arc

label HAB1:
    if music_need:
        $ renpy.music.set_volume(0.2, .5, channel="music")
    stop music fadeout 3
    scene black
    show title 006 at card_pos
    with slowfadein
    pause
    play sound "SE/Pageflip3.mp3"
    nvl clear
    
    scene bg hallway with fade
    play music "Music/Hinichi jouhe no sasoi.mp3"
    show Kanae Neutral1 at HalfRight with dissolve
    "After the lunch chime, Kanae had decided that she would return to the club room; if she were lucky, Sempai would be there! And if she weren't lucky, well, Sempai's friends were her friends, too, so that would be fine."
    show Ryo Band Neutral1 at TenthLeft with dissolve
    "But she had only made it a few steps down the hallway before a taller third year boy approached her, tape across his nose and a bruise marring his face deeply around one eye. He raised a hand in greeting before glancing around, then asked, \"Are you Michikyuu Kanae-san?\""
    nvl clear
    show Kanae Worry1
    "\"Um,\" she managed, a bit unnerved by the delinquent-looking student before her. \"Yes? Are you looking for the SOS Brigade, maybe? I'm just a new member, so I don't know much yet.\""
    nvl clear
    show Kanae Unhap3
    show Ryo Band Shifty1
    "\"No, no,\" he said, {nw}"
    show Ryo Band Shifty2
    extend "glancing around nervously, {nw}"
    show Ryo Band Shifty3
    extend "then breaking into a smile that she really didn't trust; the kind of expression she'd seen on the rude boy who chased her across dimensions. For a panicked instance, she considered sliding away ... but she couldn't do that!" 
    "Not with Sempai here, and for the first time in hundreds of worlds, someone who could help her learn how to slide better! What if she couldn't find her way back? It was still very hard, even with the practice that Yuki helped her get...."
    nvl clear
    show Ryo Band Grin2
    "\"Hey,\" he said suddenly, \"you know ... Kyon, right?\""
    show Ryo Band Grin1
    show Kanae Hap2
    "\"Sempai?\" she said, smiling. Was this boy some sort of friend of her sempai's, asking for help? Maybe that was it.... \"Yes! Is something the matter?\""
    show Ryo Band Shifty1
    show Kanae Smile1
    "\"Eh, no, I just heard....\" He trailed off and glanced around again, though the only ones around them were other students heading to their lunches, occasionally pausing to look at her or the taller boy. {nw}"
    show Ryo Band Grin2
    extend "\"Well, there is one thing,\" he allowed. \"Could you come with me for a bit...?\""
    show Ryo Band Grin1
    show Kanae Sad1
    nvl clear
    "\"I.... I think I'd better go see Sempai first,\" she decided, shaking her head."
    show Kanae Sad4
    show Ryo Band Ang1
    "The boy's face twisted in annoyance before he shook his head and declared abruptly, {nw}"
    show Ryo Band Ang2
    extend "\"I need you to come with me; your 'sempai' is causing a lot of trouble to us!\""
    nvl clear
    show Kanae Sad4
    show Ryo Band Ang1
    "At this point, all of the surrounding students had stopped moving, turning attention to the pair. "
    $ _window = True
    show Kanae Sad4 at TenthRight with move
    extend "Kanae backed up a few steps anxiously, {nw}"
    show Ryo Band Ang1 at HalfLeft with move
    extend "and when the upperclassman moved towards her, {nw}"
    hide Kanae with moveoutright
    extend "she sprinted away as quickly as she could, {nw}"
    hide Ryo with moveoutright
    scene bg ClubHallLeft with wiperight
    show Ryo Band Ang1 at TenthLeft
    show Kanae Wince1 at HalfLeft
    with moveinleft
    show Kanae Wince2
    extend "managing to make it halfway to the clubroom before he seized her shoulder {nw}"
    show Kanae Wince2:
        xalign 0.25 yalign 1.0
        linear 0.4 yalign 3.0
    play sound "SE/Thump1.wav"
    extend "and brought her down to the hallway floor. {w}She whimpered, her lunch spilling out of her bento all across the walkway, while more students crowded around. "
    $ _window = False
    show Kanae Wince2:
        xalign 0.25 yalign 3.0
        linear 0.8 yalign 1.0
    "\"Help!\" she yelled, cowering when the boy, huffing for breath, grabbed her wrist and hauled her unceremoniously to her feet."
    nvl clear
    stop music fadeout 2
    show Kanae Wince1
    show Ryo Band Ang2
    "\"Shut up,\" he snapped, glancing around and dragging her away from the spilled lunch, \"come with me before—\""
    show Ryo Band Ang1
    play music "Music/Hostiles.mp3"
    "\"You,\" a voice spat, using the rudest, most informal form of the word. "
    $ _window = True
    show Kyon Unhap4 at right with moveinright
    $ _window = False
    extend "The boy dragging her stilled, tightening his grip on her wrist as her sempai strode across the messy remnants of her lunch, eyes narrowed in annoyance. {nw}"
    show Kyon Ang2
    extend "\"Let her go.\""
    show Kyon Unhap4
    show Kanae Hap3
    "\"Sempai!\" she cheered, though her voice shook nervously."
    nvl clear
    show Kanae Smile1:
        xalign 0.4 yalign 1.0
    with fast_move
    show Kanae Wince2:
        xalign 0.4 yalign 1.0
        linear 0.1 xalign 0.25
    "The boy holding her jerked her roughly back when she tried to break free. "
    show Ryo Band Ang2
    show Kanae Wince1
    extend "\"Oh, yeah?\" he asked. \"I don't think so, not after yesterday! You're getting in way over your head, and you're about to learn a thing or two about screwing with the wrong people!\""
    nvl clear
    show Ryo Band Ang1
    show Kyon Ang4
    "\"Really?\" her sempai asked, stopping a handful of steps away from the other boy, almost within distance to reach out and grab her. He shifted his feet, rising slightly to balance on the balls of either, while constantly shifting his weight back and forth a minute distance." 
    "\"I think you're the one who's going to be in more trouble; causing a scene like this? With so many witnesses? The question in my mind is what you might hope to accomplish.\"" 
    nvl clear
    "He glanced around at the surrounding students and\nadded, {nw}"
    show Kyon Unhap2
    extend "\"Though, I'm going to admit a certain share of disappointment in the other students that none of them even {i}tried{/i} to stop you.\""
    show Kyon Unhap4
    "All of the boys in the crowd shifted their gazes to their feet, while the girls began a low murmur."
    nvl clear
    show Ryo Band Sneer1
    "\"Where's all the fight you had yesterday?\" the boy sneered. \"You swore up and down that if I dared to lay a finger on any of your 'subordinates' that you'd crush me — any time, any place. {nw}"
    show Ryo Band Ang2
    extend "Well, I don't like being played like a chump, no matter how badass you think you {i}are{/i}. You don't get the jump on me, this time.\""
    nvl clear
    show Ryo Band Ang1
    show Kyon Ang3
    "\"If I said it, it must be true,\" her sempai allowed, his gaze constantly flicking about the other boy, occasionally meeting hers. {nw}"
    show Kyon Ang4
    extend "\"But if you're any kind of man, you'll let her go and we can settle this properly.\""
    nvl clear
    show Ryo Band Ang1 
    show Kyon Unhap5 behind Kanae
    play sound "SE/lowswoosh.mp3"
    show Kanae Wince2:
        xalign 0.70 yalign 1.0
    with fast_move
    show Kyon Unhap1
    play sound "SE/impact.mp3"
    $ _window = True
    "With a sudden growl, the boy released her wrist and shoved her towards her sempai, hard. {nw}"
    show Kyon Unhap1:
        xalign 1.15 yalign 1.0
    show Kanae Wince2:
        xalign 0.85 yalign 1.0
    with fast_move
    extend "{w=0.5}Her sempai rolled back on his feet, both arms going about her as he flung himself backwards, {nw}"
    show Ryo Band Attack1 Flip
    show Kyon Unhap6 Flip:
        xalign 0.85 yalign 1.0
    show Kanae Sad2 at right
    with fast_move
    play sound "SE/impact.mp3"
    extend "twisting to take the other boy's kick on his side and shielding her with his body. {nw}"
    show Kanae Wince2:
        xalign 2.0 yalign 3.0
    show Kyon Pain1 Flip:
        xalign 2.0 yalign 3.0
    with move
    play sound "SE/slide.wav"
    extend "He landed in a slide, {nw}"
    show Kyon Unhap5:
        xalign 1.15 yalign 1.25
    with fast_move
    extend "releasing her and then rolling to his feet in a single smooth motion, crouching just over her head while the crowd around gasped quietly."
    $ _window = False
    nvl clear
    show Kyon Unhap2
    "\"Kanae-chan,\" he said, not looking at her, \"are you okay?\""
    show Kyon Unhap4
    "\"I'm okay,\" she said shakily, thinking she might have been bruised, but certainly no worse."
    show Kyon Unhap4 at HalfRight with move
    show Kyon Ang2
    "He nodded, then straightened up, stepping towards the middle of the hallway, his eyes locked on the other boy. \"Alright, you,\" he said, using the derogatory 'kisama' again, \"what the hell is your problem?\""
    nvl clear
    show Kyon Unhap4
    "The other boy growled, then surged forward, swinging a powerful punch towards her sempai. {nw}"
    play sound "SE/lowswoosh.mp3"
    $ _window = True
    show Ryo Band Attack2 Flip at center with fast_move
    show Kyon Unhap5 Flip at HalfLeft with fast_move
    show Ryo Band Attack1 at HalfRight with move:
        xanchor 0 yanchor 0
        xpos 0.5 ypos 1.0
        linear 0.4 rotate 90 
    play sound "SE/Thump1.wav"
    $ _window = False
    extend "He leaned to one side, seizing the thug's extended fist and spinning, turning all of the larger boy's force into forward momentum, flipping him completely upside-down before slamming to the floor on his back in the scattered bits of her lunch. "
    show Kyon Unhap5 Flip at TenthLeft with fast_move
    hide Ryo
    nvl clear
    "Her sempai danced away a half-step, light on his feet, hands loosely at his sides. {nw}"
    $ _window = True
    show Kanae Sup1:
        xalign 0.85 yalign 1.0
    with fast_move
    extend "Kanae quickly hopped to her feet and scurried away. {nw}"
    hide Kanae with moveoutright
    $ _window = False
    extend "Almost immediately she found herself contained in a protective circle of the girls standing on the sidelines, people she didn't know offering murmurs of sympathy and asking if she was okay. She tried not to laugh or cry at the absurdity of the situation."
    nvl clear
    "So far, only her pride and her lunch had been lost."
    nvl clear
    show Ryo Band Ang2:
        xalign 0.75 yalign 15.0
    show Ryo Band Ang2 at HalfRight with move
    "Coughing, the other boy climbed to his feet, eyes shadowed with rage, his breathing ragged and furious. \"You utter bastard!\" he spat at her sempai. \"I don't know where you get this sudden attitude, but you are in {i}way{/i} over your head! If I don't stop you here, things are only going to get worse for you!\""
    nvl clear
    show Ryo Band Ang1
    show Kyon Ser3 Flip
    "\"In that case,\" her sempai suggested in oddly reasonable tones, \"why not just give up? If you want me to suffer, wouldn't it be easier to ignore me and let your bosses, presumably people more competent than you, deal with the situation?\""
    show Kyon Ser1 Flip
    show Ryo Band Neutral1 with move:
        xalign 0.75 yalign 4.5
    "The boy growled, then sank to his knees. \"I'm powerless,\" he moaned, wrapping his arms around himself and hunching in."
    nvl clear
    show Ryo Band Shifty2
    "Shifting his shoulders, her sempai gave a terse nod and clenched one hand into a fist tightly, the crackling, snapping noises from his tendons clearly audible in the hallway. {nw}"
    show Kyon Ser2 Flip
    extend "\"Good,\" he judged. \"Now see that this never happens again.\" "
    nvl clear
    show Kyon Ser1 Flip:
        xalign -0.25 yalign 1.0
    show Ryo Band Shifty2:
        xalign 0.25 yalign 4.5
    show Kanae Unhap3 at right
    with dissolve
    show Kyon Ser1 Flip at HalfRight with move
    "He relaxed his stance and turned to Kanae; her protective circle backed away seamlessly to let him approach her, the other girls looking at him with shy smiles or bashful grins. {nw}"
    show Kyon Ser3 Flip
    extend "\"You're certain you're okay?\" he asked, putting one hand on her shoulder and focusing his full attention on her, seemingly unaware of the other students."
    nvl clear
    show Kyon Ser1 Flip
    show Kanae Sup2
    "\"Sempai!\" she shrieked, a moment too late, {nw}"
    show Ryo Band Attack1 Flip at HalfLeft with fast_move
    extend "as the other boy produced a knife from his coat and charged abruptly at her sempai."
    nvl clear
    play sound "SE/lowswoosh.mp3"
    play sound2 "SE/clink.mp3"
    show Cut with cutright
    hide Cut with fastdissolve
    show Ryo Band Attack2 Flip:
        xalign 0.6 yalign 1.0
    show Kyon Unhap5 Flip:
        xalign 0.75 yalign 5.0
    with fast_move
    show Kyon Unhap5:
        xalign 0.95 yalign 5.0
    show Kcut Fresh1:
        xalign 0.95 yalign 5.0
    show Kanae Unhap1
    "With speed she didn't think was possible, her sempai snapped his head back and threw himself to the floor, a potentially lethal stab to the side of the head reduced to a short, shallow scratch on one cheek. "
    $ _window = True
    show Ryo Band Attack1 Flip:
        xalign 0.7 yalign 1.0
    with move
    "Rolling with the momentum of his evasion, her sempai quickly righted himself and lunged, {nw}"
    show Kyon Unhap5 at HalfLeft
    show Kcut Fresh1 behind Ryo at HalfLeft
    with fast_move
    show Ryo Band Sneer1:
        xalign 0.7 yalign 1.0
        linear 0.1 xalign 0.5
    $ _window = False
    extend "grabbing the other boy's wrist and yanking him violently backwards, just as he reached for Kanae again."
    nvl clear
    $ _window = True
    show Kanae Wince1
    show Kyon Unhap5 Flip:
        xalign 0.25 yalign 1.0
        linear 0.1 xalign 0.05
    show Kcut Fresh2 Flip:
        xalign 0.25 yalign 1.0
        linear 0.1 xalign 0.05    
    play sound "SE/impact.mp3"
    show Ryo Band Sneer1:
    "This time, her sempai was more brutal, adding the boy's sudden momentum to a fierce kidney jab, {nw}"
    play sound "SE/lowswoosh.mp3"
    show Kyon Unhap5 Flip:
        xalign 0.1 yalign 2.5
    show Kcut Running1 Flip:
        xalign 0.1 yalign 2.5    
    show Ryo Band Sneer1 at HalfRight:
        xanchor 0 yanchor 0
        xpos 0.5 ypos 1.0
        linear 0.4 rotate 90
    with move
    play sound "SE/Thump1.wav"
    pause 0.2
    extend "a leg sweep, {nw}"
    play sound "SE/impact.mp3"
    play sound2 "SE/knifeslide.mp3"
    extend "then a swift kick to the hand holding the knife, {nw}"
    show Kyon Unhap5 Flip:
        xalign 0.1 yalign 1.0
    show Kcut Running1 Flip:
        xalign 0.1 yalign 1.0    
    with move
    hide Ryo
    $ _window = False
    extend "sending it clattering across the hallway through her ruined lunch, the uneasy silence of the surrounding students punctuated with a sickening crunch. The other boy howled, clutching his injured hand in agony and rolling around on his back, tears streaming from his eyes."
    nvl clear
    show Kyon Ser2 Flip
    show Kcut Running1 Flip
    "\"You,\" Kyon declared, using a more polite form and pointing at the nearest watching boy. \"See that he gets to the nurse's office.\" "
    show Kanae Worry1
    show Kyon Ser3 Flip at center
    show Kcut Running1 Flip at center
    with move
    extend "He held one hand out to her, adding, \"Let's get out of here, Kanae-chan.\""
    show Kanae Smile2
    show Kyon Ser1 Flip
    show Kcut Running1 Flip behind Kanae
    "She nervously nodded, her heart settling a tiny bit when she took his hand and he led her down the hallway."
    hide Kanae
    hide Kyon
    hide Kcut
    with moveoutright
    nvl clear
    stop music fadeout 3
    
    call eyecatch_fancy("Thursday, April 21") from HAB1_sc001
    
    scene bg ClubroomFullDay with fade:
        xpos 0 ypos 0
    $ renpy.layer_at_list([PanScene_SetToLeft])
    queue music "Music/Unzari da.mp3"
    show Koizumi Crossed Ser1 at left
    show Kanae Sad3 at center
    show Tsuruya Worry2 at center_RightScreen
    show Haruhi Crossed Worry2 at left_RightScreen
    "\"...and that's what happened,\" Kanae concluded unhappily, sniffling. \"Somehow, I caused Sempai to get hurt.\""
    $ renpy.layer_at_list([PanScene_LeftToRight])
    "\"Ah,\" Tsuruya said, her smile vanishing. \"Well, he had that cut yesterdays, so that's not your fault,\" she assured the smaller girl. \"Really, I'm the one who needs to apologize! If I weren't borrowing Kyon-kun, they wouldn't have thought that you'd be a target!\" She rose from her seat and gave a full ninety degree bow to Kanae. \"I'm sorry,\" she added."
    nvl clear
    show Kanae Sad5
    show Koizumi Sigh2
    $ renpy.layer_at_list([PanScene_RightToLeft])
    "\"A share of the blame is mine, as well,\" Koizumi added, grimacing. \"We are supposed to be watching over Michikyuu-san ... but obviously, we missed this.\""
    show Koizumi Sigh4
    show YBook at TopRight with dissolve
    "\"Logically,\" Yuki said, not raising her eyes from her book, \"this is a predetermined event. If the effect precedes the cause, responsibility becomes difficult to determine.\""
    $ renpy.layer_at_list([PanScene_LeftToRight])
    hide YBook
    show Haruhi Crossed Quest1
    show Tsuruya Worry3
    nvl clear
    "\"I'll have to ask Kyon about that later,\" Haruhi murmured. \"He's good at that stuff. Anyway, Tsuruya-san, Kanae-chan, I'm confident that Kyon will be just fine — but now I {i}really{/i} want to know what this investigation is about!\""
    nvl clear
    show Haruhi Crossed Worry2
    show Tsuruya Sigh3
    "\"Sorry,\" Tsuruya said again with a weak chuckle, only managing to smile a tiny bit as she straightened up and sat down. \"That's still top secret.... {nw}"
    show Tsuruya Hap4
    extend "Um! Kanae-chan, it isn't much, but you can have my leftover lunch, since yours got spilled! This doesn't make up for what you've suffered, but please consider it the first step of my apology!\""
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Kanae Worry3
    "\"I'm not very hungry,\" Kanae said, shaking her head uncertainly."
    nvl clear
    show Haruhi Crossed Ang2
    show Tsuruya Smile1
    $ renpy.layer_at_list([PanScene_LeftToRight])
    "\"You have to eat properly or you won't finish growing,\" Haruhi chastised. \"Hmm, I made an extra bento for.... Er, well, I made an extra bento. There should be enough to go around.\""
    show Kanae Smile1
    $ renpy.layer_at_list([PanScene_RightToLeft])    
    "Kanae nodded uncertainly, offering the other girls a weak smile. She was right to trust in her sempai, she decided. And these other new friends, while not very familiar, were the best friends she'd had in a long time...."
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Haruhi Crossed Worry2
    show Tsuruya Hap6
    nvl clear
    "\"Right, right!\" Tsuruya said brightly. \"And tomorrows, I'll escort you from your class to this clubroom for lunch! That way they'll have to deal with mes instead of you!\""
    scene bg ClubroomRightDay
    show Haruhi Crossed Worry2 at left
    show Tsuruya Smile3 at center
    nvl clear
    stop music fadeout 3
    
    call eyecatch_fancy("Thursday, April 21") from HAB1_sc002
    
    scene bg ClubHallLeft with fade
    queue music "Music/MikurunoKokoro.mp3"
    show Kyon Worry1 at right
    show Kcut Clotted at right
    show Mikuru Neutral2 at left
    with dissolve
    "His cheek still stinging, Kyon resolved to have it healed later — though by Tsuruya's unintentional hint, he knew he had the scratch before he went to help her. As much of a pain as it was (quite literally), it did establish a reasonable baseline for when he traveled back, which meant that he didn't do all of his time traveling in one big block at some future date. Though, that might build up into a daunting task...."
    nvl clear
    show Kyon Sigh1
    "\"It's like homework all over again,\" he grumbled, stopping before the Computer Research Society's room, and turning to face Mikuru. {nw}"
    show Kyon Neutral2
    extend "\"Asahina-san, can you take us back right here to ten minutes after club started yesterday?\""
    show Kyon Neutral3
    show Mikuru Think Sup1
    "\"What!?\" she yelped, before blinking, bowing her head. {nw}"
    show Mikuru Think Sad1 
    extend "\"O...oh, right.... Um, yes, but shouldn't we go to the nurse's office first?\""
    nvl clear
    show Mikuru Think Sad3
    show Kyon Neutral2
    "\"It'll be fine,\" he assured her. \"According to Tsuruya, she bandages this cut herself, so....\""
    show Kyon Neutral3
    show Mikuru Think Quest1
    show MBlush Think at left
    "\"Okay,\" she agreed anxiously, raising her hands to place them on his shoulders, her face reddening as she turned to gaze away. \"Um ... please close your eyes....\""
    scene almostblack two with fade
    "He did as she instructed, and time around them collapsed. It felt like part of the nauseating lurch that Yuki had invoked when she made her training dimensions, but only a small part, and when his feet steadied, he looked around recognizing the hallway easily." 
    nvl clear
    scene bg ClubHallLeft with fade   
    show Mikuru Think Sad3 at left
    show MBlush Think at left
    show Kyon Neutral1 at right
    show Kcut Clotted at right
    with dissolve
    "\"We made it?\" he asked, as Mikuru hesitantly lowered her hands, her face still red."
    show Kyon Neutral4
    show Mikuru Think Quest2
    "\"Y...yes,\" she agreed, checking her wristwatch. \"W...what do we do now?\""
    nvl clear
    show Mikuru Think Quest3
    show Kyon Neutral2
    "\"Ah ... I think you'll want to hide,\" he suggested, considering that he didn't want to make Mikuru watch him fight. Hell, he didn't particularly want to fight! But that boy.... \"Do you think the calligraphy club would mind you dropping in for a day?\""
    show Kyon Neutral3
    show Mikuru Think Quest1
    "\"N...no,\" she agreed. \"I suppose they wouldn't....\""
    nvl clear
    show Mikuru Think Quest4
    show Kyon Smile6
    "\"Good,\" he decided. \"You should be safe there.\" {nw}"
    show Kyon Neutral3
    extend "After a moment of thought, he reached into his pocket and pulled out his cell phone, turning it off. If his memory was correct, his past self should just be leaving the school to enter the car with Mori. He didn't remember receiving any calls, but better safe than sorry."
    nvl clear
    hide Mikuru
    hide MBlush
    with moveoutright
    "She gave a hesitant nod and dashed down the hall to the classroom in question, shooting a worried glance over her shoulder at him. {nw}"
    $ _window = True
    show Tsuruya Wave Hap1 at left with moveinleft
    stop music fadeout 1
    play music "Music/suspicion.ogg"
    $ _window = False
    extend "Just as she vanished from sight, Tsuruya finished her own dash up the stairs into the clubroom corridor, her eyes widening excitedly. \"Kyon-kun,\" she caroled, but in a quiet voice, drawing out the honorific. \"Hey, hey, would it be okay if I borrowed you a bit for helps with my investigation?\""
    nvl clear
    show Tsuruya Sup1 Flip
    "She blinked suddenly, pausing to stare his cheek, then frowned sharply. \"Ooh, you better come with me, first of all,\" she decided, seizing his wrist and leading him back into the school. {nw}" 
    $ _window = True
    scene bg LockersDayLeft with wiperight
    show Tsuruya Smile2 Flip at left with dissolve
    $ _window = False
    extend "He followed in bemusement until they reached her locker and she produced a first aid kit, cleaning his wound and then applying a bandage."
    nvl clear
    show Tsuruya Hap1 Flip with None
    show Kyon Smile4 at right
    show Kcut Bandage at right
    with dissolve
    "\"There,\" she said, once her treatment was done, grinning again. There was a twinkle in her eyes as she added, \"Don't get a scar, unless you gets another one to make it cross-shaped. That makes you way more rugged and bish!\""
    show Tsuruya Smile3 Flip
    show Kyon Smile6
    "\"Yeah, that's not the part I'm worried about,\" he said, smirking, though the expression vanished the moment his cheek pulled at the cut. {nw}"
    show Kyon Neutral2
    extend "\"Anyway, Haruhi won't mind me helping you out; I've been dismissed from club activities today.\""
    nvl clear
    show Kyon Neutral3
    show Tsuruya Hap5 Flip
    "\"Oh! Perfects! We can keep on with our investigation!\" Tsuruya said excitedly, glancing around to make sure that no one was within eavesdropping distance."
    show Tsuruya Grin4 Flip
    "\"Okies, here's what I've found out so far ... those pushy fellows from Sunday, they have a contact in the school, a third year named Ryuguu Ryo-san. He loiters around on the campus behind the gym after school to make his deals. I want to questions him, but he's a big fellow, and Kasai's out ... so if you don't minds, could you be my muscle for a bit?\""
    nvl clear
    show Tsuruya Grin2 Flip
    show Kyon Ser3      
    "\"Sure,\" Kyon agreed, realizing that the boy he had just fought with (from his perspective) must have been Ryuguu. Well, the informal 'you' would still serve for him. \"So, any plan? Maybe a little good cop, bad cop?\""
    show Tsuruya Hap1 Flip
    show Kyon Ser1
    "Tsuruya giggled, leading the way to the shoe lockers and changing. Kyon checked his locker, but of course, the only shoes there were yesterday's indoor shoes."
    show Kyon Sigh3
    "\"I should have remembered that,\" he grumbled to himself. " 
    nvl clear
    scene bg SchoolOutside with fade
    "Shaking his head, he followed Tsuruya out of the school building and around to the gym, to the shady side where the physical education storage outbuildings were. The stereotypical location for illicit romances within the school, delinquents hiding out...."
    show Tsuruya Ser1 Flip at left with dissolve
    nvl clear
    "\"Now, I don't know Ryuguu-san, because we don't share a class together,\" Tsuruya warned in a whisper, \"but how many people are there hanging out around here?\""
    nvl clear
    hide Tsuruya with dissolve
    show Ryo Neutral1 at center with dissolve
    "It took a moment, but Kyon was able to pick out the boy in question, somewhat unfamiliar without tape across his nose and one eye blackened. \"That's him,\" Kyon told her with a nod. \"I've seen him before.\" Tsuruya leapt into a thicket of bushes and he followed, almost landing on her, murmuring a quick apology beneath his breath as they crept forward to watch Ryuguu and his allies."
    nvl clear
    show Yamane Grin3 at right with dissolve
    "One of them Kyon knew — Yamane, from his own class, a shady looking character in his own right. Physically, the\nboy was as intimidating as Kunikida, and had large, round glasses and shadowed eyes, cursing him with the appearance and bearing of a sad otaku. {nw}"
    #show Manabe at left with dissolve
    extend "The other one was a taller, thin first year with blond hair. Both were carrying cameras and speaking with Ryuguu in low tones."
    nvl clear
    "He couldn't pick out more than the occasional tone of voice; words weren't carrying at this distance. At a glance, Tsuruya was staring intently, mouthing occasional words to herself and giving slight nods. Kyon was taken aback; could she read lips? {nw}"
    $ _window = True
    hide Yamane Neutral with dissolve
    #hide Manabe with dissolve
    $ _window = False
    extend " \"Okay,\" she whispered, when Yamane shook his head sharply and turned away, leaving the older boy with the first year in tow. \"Once they're gone, let's go talk to him, okay?\""
    "\"Do you know what they were talking about?\" he whispered back."
    hide Ryo with dissolve
    nvl clear
    show Tsuruya Neutral1 Flip at left
    show Kyon Ser1 at right
    show Kcut Bandage at right
    with dissolve
    "\"I'm not that goods yet,\" Tsuruya said apologetically, giggling very quietly. \"But I got that Ryuguu-san is mad at the other twos. Somethings went wrong, probably what we did on Sunday, so Ryuguu-san's having trouble, and the other two.... "
    "Hmm. The one with glasses said something about not caring about Ryuguu-san's problems, and that he still wanted money. I guess Ryuguu-san must owe him something.... The first year student was just following along, doing what he was tolds; he doesn't seem to be as high up on the food chains.\""
    nvl clear
    show Tsuruya Neutral2 Flip
    show Kyon Ser3
    "\"The one with glasses is Yamane-san, from my own class,\" Kyon said helpfully. \"I think he's in the photography club? I know he takes a lot of pictures during school events.\""
    show Kyon Ser1
    show Tsuruya Susp1 Flip
    "\"Hmm, so he's probably a foreman or one of the workers,\" Tsuruya mused, eyes sharpening. \"Okies, they're gone; let's get Ryuguu-san before anyone else shows up or he leaves.\""
    show Tsuruya Smile1 at center with move
    show Ryo Neutral1 Flip at left with dissolve
    nvl clear
    "Kyon nodded at her, and the pair stood up, walking out of the bush and brushing leaves off. Ryuguu saw them emerge and jolted a bit, then crossed his arms over his chest and scowled. {nw}"
    show Ryo Ang1 Flip
    extend "\"What?\" he snapped, the moment they drew within hearing range."
    nvl clear
    show Kyon Ser1
    "Uncertain of his role, Kyon just took up the loose, relaxed stance he had used when fighting Ryuguu last time, and said nothing."
    show Tsuruya Hap4
    "\"How's business?\" Tsuruya asked, suddenly politely professional."
    show Ryo Neutral1 Flip
    show Tsuruya Smile2
    "Ryuguu frowned, then said, \"Shouldn't be any of yours.... But.... Well, I heard you were a bit ... strange, Tsuruya-san. So, you want to buy?\""
    nvl clear
    show Tsuruya Hap5
    "\"Maybe,\" Tsuruya allowed. \"Whatcha got?\""
    show Ryo Shifty2 Flip
    show Tsuruya Smile1
    "\"If you don't know, I'm not selling.\""
    show Tsuruya Grin6
    "\"Oh, I knows what you're selling,\" she said evenly. \"Hum.... Anything from this year's students?\""
    nvl clear
    show Ryo Neutral1 Flip
    show Tsuruya Grin4
    "\"A bit,\" Ryuguu allowed, dropping his hands to his sides. \"Now, look, I'll sell to you, but only because my normal distributor is having problems. Understand that this is top-shelf stuff, meant to be shipped to the highest paying customers and then resold. So that's the kind of price I'm looking for. No copy protection, no censorship — this is the real deal.\""
    nvl clear
    show Kyon Blink
    "Kyon blinked, wondering what the hell was going on, but deciding he already didn't like it. He tried to keep his expression neutral."
    show Tsuruya Grin5
    "\"So, what's the price?\" Tsuruya asked, grinning. \"I didn't bring a checkbook with me, nyoro~!\""
    show Ryo Grin1 Flip
    show Tsuruya Grin2
    nvl clear
    "\"Right now I've got three SD cards, sorted by year,\" Ryuguu said, shifting his speech pattern from 'thug' to 'semi-competent salesman'. He fanned out the three cards between his fingertips, turning them back and forth to show Tsuruya both sides of the small digital chips. \"First year, twenty thousand yen, second year, fifteen thousand, third year, fifteen thousand.\""
    show Tsuruya Hap4
    "\"And these are sources?\" Tsuruya pressed. \"Originals, so there's no copies?\""
    nvl clear
    show Ryo Grin2 Flip
    show Tsuruya Smile1
    "\"What, you want them exclusively?\" Ryuguu asked, quirking one eyebrow up in a smirk."
    show Ryo Shifty1 Flip
    show Tsuruya Grin6
    "Tsuruya nodded quickly. \"Think about it,\" she said. \"If I'm paying to be a reseller, what's the point if the next guys comes along and buys them then undercuts me? Yous got to be a sharp businessman to make it here, don'tcha?\""
    show Ryo Shifty2 Flip
    show Tsuruya Grin3
    nvl clear
    "\"Double the price,\" he said, shrugging. {nw}"
    show Ryo Shifty3 Flip
    extend "\"Then, sure, I'll give you everything and exclusive distribution. Only caveat is that I'm absolutely keeping personal copies.\""
    show Tsuruya Grin5
    "\"Hmm,\" Tsuruya replied, touching one fingertip to her lips and gazing upward, musing. \"Well, one hundred thousand yens is rather a lot, don'tcha think? Especially since I'm trying to see if I'm in the third years?\" She turned to Kyon and asked, \"Should we apply our discount?\""
    show Ryo Shifty2 Flip
    show Kyon Ser3
    show Tsuruya Grin2
    nvl clear
    "\"Yeah,\" Kyon agreed, nodding. \"I think we can negotiate a better price.\""
    show Ryo Neutral1 Flip
    show Kyon Ser1
    "\"Oh, don't even think about it,\" Ryuguu retorted, waving a hand dismissively. \"I'm the one holding the cards here, so to speak. There's no way that—\""
    show Tsuruya Grin4
    stop music fadeout 1
    queue music "Music/KamadoumaEnd.mp3"
    nvl clear
    $ _window = True
    "Tsuruya's hand darted out, lightning-fast, and she snatched two of the cards from Ryuguu's grasp before the boy could react. {nw}"
    show Ryo Attack1 Flip
    extend "Immediately his face went red, and his scowl turned murderous. {nw}"
    show Ryo Attack1 Flip at TenthLeft with fast_move
    $ _window = False
    extend "He launched a punch towards the tall girl in retaliation, growling from low in his throat."
    nvl clear
    $ _window = True
    show Tsuruya Sup1:
        xalign 1.0 yalign 1.4
    show Kyon Unhap5 at HalfRight
    show Kcut Bandage at HalfRight
    with rapid_move
    play sound "SE/lowswoosh.mp3"
    pause 0.2
    play sound "SE/impact.mp3"
    "Already waiting for such an opening, Kyon grabbed the extended fist as Ryuguu attacked, while Tsuruya ducked away. {nw}"
    play sound "SE/impact.mp3"
    show Kyon Unhap5 at HalfLeft
    show Kcut Bandage at HalfLeft
    show Ryo Ang1:
        xalign -0.2 yalign 1.0
    with rapid_move
    $ _window = False
    extend "Giving an unbalancing wrench to the captured appendage, Kyon pulled Ryuguu off balance and spun him around before shoving the boy violently forward, his arm pinned behind his back at an awkward angle. The third year boy's nose smashed into the equipment shed behind him, making a loud crunch and sending a spray of blood out."
    nvl clear
    show Tsuruya Ang1
    "\"Gwah!\" Ryuguu choked out, his free hand scrabbling at the wall of the shed. \"What the fu—\""
    play sound "SE/impact.mp3"
    show Ryo Ang1:
        xalign 0.0 yalign 1.0
        linear 0.1 xalign -0.2
    show Kyon Ang3
    "Kyon jerked him away from the wall and shoved him forward again, resulting in another meaty smash. \"Free is sounding like a good price to me right now,\" he managed, struggling to calm himself and keep the fury from his voice. \"You,\" he said, gladly falling back onto the course informal version of the word, \"need to understand something here."
    nvl clear
    show Kyon Ang2
    "\"You are not the biggest business in this school, or this town. There are certain people in this school you {i}do not{/i} screw with. If you ever even {i}think{/i} of laying a finger on any of my subordinates, or interfering with any of them in any way, believe me, this is going to be the {i}least{/i} of your worries.\nAny time, any place — I will not allow it.\" "
    nvl clear
    show Kyon Unhap5 at center
    show Kcut Bandage at center
    show Ryo Attack1 at left
    with move
    "He pulled the boy back, spinning him around, and when Ryuguu belatedly tried to punch with his free hand, {nw}"
    show Ryo Attack2 Flip
    play sound "SE/lowswoosh.mp3"
    $ _window = True
    show Kyon Unhap5:
        xalign 0.5 yalign 1.0
        linear 0.2 yalign 1.5
    show Kcut Bandage:
        xalign 0.5 yalign 1.0
        linear 0.2 yalign 1.5
    pause 0.2
    extend "he tilted his head to one side, narrowly dodging the blow {nw}"
    play sound "SE/impact.mp3"
    pause 0.15
    show Ryo Attack1 with rapid_move:
        xalign -0.2 yalign 1.0
    play sound "SE/impact.mp3"
    pause 0.2
    show Ryo Ang1 with slow_move:
        xalign -0.2 yalign 20.0
    play sound "SE/Thump1.wav"
    hide Ryo
    $ _window = False
    extend "and returning a much stronger one, which sent the upperclassman smashing back into the shed, eyes rolling up before he collapsed."
    nvl clear
    show Kyon Unhap5:
        xalign 0.5 yalign 1.5
        linear 0.2 yalign 1.0
    show Kcut Bandage:
        xalign 0.5 yalign 1.5
        linear 0.2 yalign 1.0
    show Tsuruya Sup1
    "\"Yow,\" Tsuruya allowed, eyes wide. \"You okay there, Kyon-kun?\" {nw}"
    $ _window = True
    show Tsuruya Ang3:
        linear 0.2 xalign 0.08 yalign 2.44
    show Kyon Unhap5 at HalfRight
    show Kcut Bandage at HalfRight
    with fast_move
    $ _window = False
    extend "Despite her question, her attention was on the prone boy as she crouched, rifling through his pockets and pulling out a small stack of mini-discs and SD cards. \"We could have gotten more answers out of him, you knows....\""
    show Kyon Sigh1
    "\"Still can,\" Kyon pointed out, cracking his neck and expelling a long sigh. \"Sorry. This guy ... really pisses me off.\""
    nvl clear
    show Kyon Sigh3
    show Tsuruya Ser1
    "\"Understandable,\" Tsuruya agreed, turning her attention to the bag at Ryuguu's side, pulling more media and a digital camera from within, transferring everything to her own bag. \"So, I don't think good cops bad cops will cut it here....\""
    show Tsuruya Hap5
    nvl clear
    "Tsuruya tapped her chin thoughtfully, then pulled off the prone Ryugu's belt and tightly bound his wrists before him. \"Okies!\" she said decisively. \"We'll go with bad cop worse cop! You be worse cop, so just stand over there and look real angry at him! I betcha that'd scare most anyones.\""
    nvl clear
    show Kyon Unhap4
    "Kyon took a breath and did as she instructed, having no trouble maintaining his glower at the prone boy as Tsuruya cheerfully slapped him awake, ignoring the blood flowing\nfrom Ryuguu's nose. \"Wakey-wakey!\" Tsuruya called, {nw}"
    $ _window = True
    show Tsuruya Hap5:
        xalign 0.08 yalign 2.44
        linear 0.2 xalign 1.0 yalign 1.0
    show Kyon Unhap4 at center
    show Kcut Bandage at center
    with move
    $ _window = False
    extend "stepping back when Ryuguu jerked awake and tried to fumble for her."
    "\"Okies! Now, you want to answers some of my questions, or maybe let Kyon-kun heres give you some more manual attitude adjustments?\""
    nvl clear
    show Tsuruya Grin2
    "\"Wha,\" he managed, wincing. \"What are you.... Hey! I don't have to take this! I've got friends high up! You do not know who you're messing with!\""
    show Tsuruya Ang3
    "\"Neither do you,\" Tsuruya retorted. \"But, like Kyon-kun said, there are some peoples you just don't mess with! And some of those peoples are the Tsuruya family! Which means you've already screwed up!\""
    nvl clear
    show Tsuruya Ang1
    show Kyon Unhap5
    "Kyon obligingly cracked his knuckles slowly, one at a time, his gaze locked on the upperclassman's eyes."
    nvl clear
    "Ryuguu shivered, then blurted out, \"Fine! Take everything I have! I'm just a middle-man; it's all on your own damn heads if you piss off my big brothers! But because I'm just a middle-man, I don't know anything! I collect and distribute, but that's {i}it{/i}! I don't know how everyone works; they do their own things, and as long as we get our goods, we don't ask questions!\""
    nvl clear
    show Tsuruya Ser1
    "\"That first years you were talking with,\" Tsuruya said primly. \"What's his name?\""
    show Tsuruya Ang1
    "\"T...that.... Manabe Satoshi, class 1-7,\" Ryuguu said, sweating nervously."
    show Tsuruya Ser1
    "\"Good! Good! And who else...?\""
    show Tsuruya Ang1
    "\"Just him and Yamane Jun, class 2-5,\" Ryuguu whimpered. \"I swear! They handle everything else! I'm just a go-between!\""
    nvl clear
    show Tsuruya Neutral1
    "\"Hmm, hmm,\" Tsuruya noised, nodding. \"And on the other sides? You collects from those two, who do you sells to?\""
    show Tsuruya Neutral2
    "\"T...that's.... They aren't around anymore,\" Ryuguu said, sweating. \"They got arrested on Sunday! I'm still looking—\""
    show Tsuruya Ang4
    "\"{i}Wrong{/i}!\" she yelled in his face."
    nvl clear
    show Tsuruya Ang2
    "\"W...was looking,\" Ryuguu allowed, shaking, \"f...for a new distributor to sell to!\""
    show Kyon Ang2
    "\"'Was' is right,\" Kyon interjected. \"I think we all understand that you're {i}done{/i} with this, if you know what's good for you.\" Though, given what he already knew was going to happen tomorrow...."
    show Kyon Unhap4
    show Tsuruya Grin6
    "\"Alright,\" Tsuruya said, nodding as she rose from her crouching position to her feet. \"Kyon-kun, put him to sleep again.\""
    nvl clear
    show Tsuruya Grin4
    show Kyon Ser1
    "Kyon nodded, stepping around Ryuguu's weakly flailing arms and easily wrapping the boy's neck in a choke-hold, which he held until Ryuguu passed out. {nw}"
    show Kyon Sigh1
    extend "Once the upperclassman was prone on the ground, he took a deep breath and closed his eyes, double-checking to see that the bigger boy still had a pulse. {nw}"
    stop music fadeout 3
    show Kyon Smile6 Flip
    show Kcut Bandage Flip
    extend "\"Sorry,\" he told Tsuruya, opening his eyes as he rose and giving her a weak smile. \"This is.... It's....\""
    nvl clear
    queue music "Music/MikurunoKokoro.mp3"
    show Kyon Smile1 Flip
    show Tsuruya Hap7 with move:
        xalign 0.85 yalign 1.0
    "He was surprised when Tsuruya leaned into him, giving a tight hug. \"It's okay,\" she said soothingly, patting his head."
    "\"This kinds of detective work is enough to turn even someone like you hot blooded! And that's fine; Haru-nyan is in good hands! Since you're helping me out, I am too!\""
    nvl clear
    show Tsuruya Smile4
    show Kyon Smile2 Flip
    "He hesitantly hugged her back, realizing the source for the 'two-timing' rumor. Obviously, someone was within range to see all this.... {nw}"
    show Kyon Smile7 Flip
    extend "\"Thanks, Tsuruya-sempai,\" he managed, the upperclassman's friendly embrace banishing his anger. \"A...anyway, like I said, any time you need help with this investigation, let me know.\""
    show Kyon Smile2 Flip
    show Tsuruya Hap4 at right with move
    nvl clear
    "\"You got it!\" she enthused, breaking the contact and grinning at him. \"I'll start investigatings those other two! But it's a lot bigger than just the two of them.... Which one do you think we should go after first?\""
    show Tsuruya Smile2
    show Kyon Puzzle1 Flip
    "\"Kanae-chan is in class 1-7,\" he said, frowning. \"I'm a bit worried about her....\""
    show Kyon Worry1 Flip
    show Tsuruya Hap5
    "\"You got it,\" Tsuruya agreed. \"Satoshi-san should be easier to shake down than Ryuguu-san, here.\""
    nvl clear
    scene bg SchoolEntranceLeft with fade
    show Tsuruya Smile2 at HalfRight
    show Kyon Neutral2 Flip at left
    show Kcut Bandage Flip at left
    with dissolve
    "He followed Tsuruya back to the school entrance, nodding at her. \"Okay, you take care,\" he told her. \"I've got to get back ... uh ... to Haruhi.\""
    nvl clear
    show Kyon Neutral3 Flip
    show Tsuruya Grin6
    "\"I thought you were dismissed from the club today?\" she asked, raising one eyebrow and smirking."
    show Tsuruya Grin3
    show Kyon Unhap6 Flip
    "\"Oh, yeah,\" he agreed, frowning. \"Well, I have to head back\nin anyway, since {nw}"
    show Kyon Puzzle1 Flip
    extend "... I forgot my shoes. Yeah. I'll see you tomorrow, alright, Tsuruya-sempai?\""
    nvl clear
    show Kyon Worry1 Flip
    show Tsuruya Hap1
    "\"Hehe, you can just call me Tsuruya,\" she said with a wink, glancing at his indoor shoes. \"I'd let you get away with more, but I don't want Haru-nyan to get the wrong idea!\""
    show Tsuruya Smile2
    show Kyon Smile3 Flip
    "\"How about Tsuruya-kun?\" he asked, {nw}"
    show Kyon Smile2 Flip
    extend "smirking before the twinge from his cut reminded him why he shouldn't."
    show Tsuruya Hap7
    "\"I like it!\" she approved, nodding vigorously. \"We're working on this investigation togethers!\""
    nvl clear
    show Tsuruya Smile4
    show Kyon Smile7 Flip
    "\"You got it,\" he agreed, nodding back. \"Take care, Tsuruya-kun.\""
    show Kyon Smile2 Flip
    show Tsuruya Hap5
    "\"You too, Kyon-kun!\" she called back, waving as she strode towards the school gates."
    nvl clear
    scene bg ClubHallLeft with fade
    "After scraping as much of the mud and dirt from his indoor shoes as he could, Kyon trudged wearily to the club house, taking the longer route to avoid encountering anyone being released from the club meeting."
    play sound "SE/doorknock.mp3"
    "He knocked on the calligraphy clubroom door, pleased when Mikuru answered, bowing and excusing herself from her impromptu meeting with her former club members."
    nvl clear
    show Kyon Neutral2 at TenthRight
    show Kcut Bandage at TenthRight
    show Mikuru Think Quest3 at TenthLeft
    with dissolve
    "\"How did everything go?\" he asked, once they were alone in the hallway."
    show Kyon Neutral3
    show Mikuru Think Quest2
    "\"Fine!\" she said anxiously, peering at the bandage on his face. \"The nurse said you were okay?\""
    nvl clear
    show Kyon Sigh5
    show Mikuru Think Quest3
    "\"I'll be fine,\" he assured her, grinning. \"Okay, um, we need to return to tomorrow ... can you take us to the clubroom, say ... two minutes before the bell at the end of lunch? That should be enough time to get back to class.\""
    show Kyon Smile4
    show Mikuru Smile3
    "\"Okay,\" she agreed, her eyes unfocusing briefly before she turned to face him, placing a hand on either shoulder. \"Close your eyes,\" she reminded him, as always."
    nvl clear
    scene almostblack two with fade
    scene bg ClubroomRightDay with fade
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
    $ renpy.layer_at_list([PanScene_SetToRight])
    show Kyon Smile4 at center_RightScreen
    show Kcut Bandage at center_RightScreen
    show Mikuru Smile2 at right_RightScreen
    show Yuki Side1 at left_RightScreen
    with dissolve
    "After completing the temporal transition, Mikuru lowered her hands from his shoulders, and Kyon's eyes opened, glancing around the clubroom. Unsurprisingly, Yuki was the only club member still left in the room."
    "She closed her book and rose, moving to Kyon's side and raising one hand to his cheek briefly. He blinked, then grinned at the girl, tracing his fingertips across the bandage but leaving it in place. {nw}"
    show Kyon Smile6
    extend "\"Thanks, Nagato,\" he said, nodding at her. \"And thank you, too, Asahina-san.\""
    nvl clear
    show Kyon Smile4
    show Yuki Talk1
    "\"It is no problem,\" Yuki returned smoothly."
    show Yuki Side1
    show Mikuru Quest1
    "\"No trouble at all,\" Mikuru agreed, even though she had butterflies in her stomach just from remembering Kyon bleeding. It wasn't as bad as the time she'd seen him {i}stabbed{/i}, but she didn't have to like it one bit!"
    show Mikuru Neutral1
    show Kyon Puzzle1
    play sound "SE/doorknock.mp3"
    "A knock sounded on the door, and Kyon turned around, pondering, \"Who could that be...?\""
    nvl clear
    stop music fadeout 1
    play sound "SE/dooropenfast.wav"
    queue music "Music/WitchInGoldCenba.ogg"
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Koizumi Think Sigh1 at left with dissolve
    "After a heartbeat, the door opened and Koizumi peered in, sighing with relief as he saw Kyon, though there was still tension in his gaze. \"I'm afraid I have some bad news, Kyon-kun,\" he said, smiling weakly. \"Ah ... school administration would like to speak with you ... {nw}"
    show Koizumi Think Ser2
    extend "though it seems that some strings were pulled, and the issue was somehow moved down to a meeting with the Student Council President. There's an emergency session now, so....\""
    nvl clear
    show Koizumi Think Ser1 with None
    show Kyon Sup2 at right
    show Kcut Bandage at right
    with dissolve
    "\"Really?\" Kyon asked, surprised. \"I'm not sure what's stranger. That the Student Council can handle cases like this, or that they get to skip classes for it. {nw}"
    show Kyon Neutral2
    extend "Well, whatever.\""
    show Kyon Neutral3
    show Koizumi Think Ser4
    "\"Don't forget, Kimidori Emiri will be there,\" Koizumi warned with a frown. \"Which probably explains {i}how{/i} the Student Council was given authority for this meeting.\""
    $ renpy.layer_at_list([PanScene_LeftToRight])
    nvl clear
    show Yuki Talk1
    "\"I will go,\" Yuki declared, her eyes fixed on Kyon."
    show Yuki Side1
    show Mikuru Think Sup1
    "\"M...me too,\" Mikuru managed, wishing she could sound as confident as Yuki."
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Koizumi Think Grin2
    "\"And naturally,\" Koizumi agreed, bowing slightly, \"I will be at your side as well.\""
    nvl clear
    show Koizumi Think Grin1
    show Kyon Unhap2
    "\"Okay, let's go,\" Kyon decided. \"Haruhi's going to burst into the middle of the meeting and be really pissed off about not being involved.\""
    show Kyon Unhap4
    show Koizumi Think Sup1
    "\"Ah.... You're certain?\" Koizumi asked."
    nvl clear
    show Koizumi Think Worry1
    show Kyon Sigh2
    "Kyon nodded, turning his cell phone back on. \"She absolutely will if you send a text to her just before we enter the Student Council room,\" he said."
    "\"That should give Kimidori-san enough time to state her goals and reasons, but not to actually {i}do{/i} anything before Haruhi shows up. And despite what they've done so far, I doubt that Kimidori-san is stupid enough to try something in front of Haruhi.\""
    nvl clear
    show Kyon Sigh4
    show Koizumi Think Grin2
    "\"Good strategy,\" Koizumi agreed, preparing the text message and falling into file behind Kyon as he led the way to the club room. Yuki stood perfectly at his side, taking every step with the boy, and Mikuru fought down another surge of jealousy at the interface's confidence."
    nvl clear
    scene bg StudentCouncil with fade
    stop music fadeout 1
    queue music "Music/MysteryTime.mp3"
    play sound "SE/dooropenfast.wav"
    show Kyon Ser1 Flip:
        xalign 0.4 yalign 1.0
    show Kcut Bandage Flip:
        xalign 0.4 yalign 1.0
    show Koizumi Crossed Neutral1 at left behind Kyon
    show Yuki Ang1 behind Kyon:
        xalign 0.7 yalign 1.0
    with dissolve
    "Kyon marched to the door and flung it open without knocking, startling the Student Council president as he shuffled through a short stack of papers. Kimidori Emiri sat in a chair to one side, her pad of paper and pen ready, though she seemed coolly expectant."
    nvl clear
    "Kyon strode to the middle of the room and stood in an arrogant pose, arms crossed over his chest as he stared down at the president with an expression of clear boredom. Yuki stood a half-step behind him on his left, eyes fixed on Emiri. {nw}"
    play sound "SE/doorclose2.mp3"
    $ _window = True
    show Mikuru Neutral1 at right behind Yuki with dissolve
    $ _window = False
    extend "Mikuru tried to take up a flanking position on his right, but was beaten by Koizumi, so settled for closing the door and standing next to Yuki."
    nvl clear
    show Kyon Unhap2 Flip
    "\"Well?\" Kyon demanded, when the president spent a long moment staring. \"I'm here.\""
    hide Yuki
    hide Mikuru
    with dissolve
    #show President at right with dissolve - Irritated with frown
    show Kyon Unhap4 Flip
    "\"I don't...\" the president began, frowning and scanning across the group. \"I expected you to bring her along, if you were going to appear in force.\""
    nvl clear
    show Kyon Neutral2 Flip
    #show President - Irritated with frown, mouth closed
    "\"Yeah, okay,\" Kyon allowed, relaxing his arms and taking on his more normal demeanor. \"So, do you have anything for me, President, or is this Kimidori-san's call?\""
    nvl clear
    #hide President
    show Kimidori Smile Flip at right #Open mouth
    with dissolve
    show Kyon Neutral3 Flip
    "Emiri smiled awkwardly and set her pen down. \"Currently, everything here is within the technical limitations of the Student Council's jurisdiction,\" she explained. \"I do not plan to usurp the president; I'm merely a secretary.\""
    nvl clear
    show Kyon Ser2 Flip
    show Kimidori Smile Flip
    "\"I really have no patience for intrigue, just now. I'm in the middle of an investigation that I'm honestly ashamed to find out you're doing nothing about,\" he said pointedly, staring at Emiri."
    nvl clear
    show Kyon Ser1 Flip
    show Kimidori Confused Flip
    "Emiri looked confused and shook her head. \"I'm sorry, I'm afraid I don't understand....\""
    hide Kimidori
    #show President at right - Neutral with frown
    with dissolve
    "\"This attitude doesn't become you,\" the president added with a frown at Kyon. \"My job is to keep Suzumiya-kun in line, not {i}you{/i}. Koizumi-kun, what's this all about?\""
    nvl clear
    show Koizumi Crossed Smile3
    #show President - Neutral with frown, mouth closed
    "\"Difficult to explain quickly,\" the esper said with a bright smile. \"For the moment, however, I answer to Kyon-kun as my superior ... and realistically, you probably should as well.\""
    show Koizumi Crossed Smile1
    "Emiri blinked several times, her awkward smile slipping."
    nvl clear
    #show President - Surprise, mild version
    "\"Really?\" the president asked, raising an eyebrow. "
    #show President - Annoyed
    extend "\"Well, in that case,\" he asked sardonically, turning his attention back to Kyon, \"what's the plan?\""
    show Kyon Neutral2 Flip
    #show President - Annoyed, mouth closed
    "\"Let's start with how much trouble I'm in for protecting Kanae-chan from that pervert,\" Kyon suggested."
    nvl clear
    show Kyon Neutral3 Flip
    #show President - Neutral
    "\"Technically none,\" the president admitted. \"It's a behavior issue, but all accounts indicate you in self defense, or in defense of a classmate. Ryuguu-san is already being expelled just on the grounds of bringing a weapon into the school and assaulting fellow students ... though he was taken away in an ambulance. "
    nvl clear
    "In any event, because of that, orders were handed down from the principal to discuss your behavior.... I have the authority to demand a meeting with an advisor for you — several if I believe that your behavior is likely to become problematic. Okabe-sensei is your advisor, right?\""
    nvl clear
    show Kyon Unhap1 Flip
    #show President - Neutral with frown, mouth closed
    "Kyon grimaced. {nw}"
    show Kyon Sigh1 Flip
    extend "\"Don't get me wrong, he's a good guy, but I'm not exactly eager for that,\" he said. \"My family?\""
    show Kyon Sigh3 Flip
    #show President - Neutral, closed eyes
    "\"Already notified,\" the president said, almost apologetically. \"The administrative staff did that first thing.\""
    nvl clear
    show Kyon Sigh1 Flip
    #show President - Neutral, open eyes, closed mouth
    "\"Figured. Alright. So, I'm going to tell you right now, when this is over, you're actually going to thank me for what I\ndid today, and what's going to happen in the coming days.\" {nw}"
    #hide President
    show Kimidori Neutral Flip at right
    with dissolve
    show Kyon Ser2 Flip
    extend "Turning his full attention to Emiri, he added, \"Seeing as I'm not up for intrigue at the moment, can you cut to the chase and say {i}why{/i} you've pulled the strings you have to arrange this?\""
    nvl clear
    show Kyon Ser1 Flip
    show Kimidori Sigh Flip
    "Emiri sighed, shifting her shoulders uncomfortably. \"You are becoming a bit troublesome,\" she allowed, shaking her head. "
    show Kimidori Unhap Flip #open mouth
    extend "\"I wanted to relate to you in clear terms that all else aside, the entity has not deviated from their chosen course of action.\""
    show Kyon Sigh2 Flip
    "\"That's a real pity,\" Kyon sighed. \"I didn't want us to be enemies.\""
    nvl clear
    show Kyon Sigh4 Flip
    show Kimidori Neutral Flip
    "\"Well, you made your decision,\" Emiri said with an apologetic shrug. \"I, personally, mean you no harm. My role has naturally changed, as I am denied administrative access over Nagato Yuki. For the time being, despite our differences concerning this issue at large, I wish to remain as neutral as possible to function as negotiator between yourselves and the entity."
    nvl clear
    "Until such time as you inform me otherwise, I will assume that you continue to maintain your stance. However ... should things change and you decide to side with us, the entity also holds no enmity against you.\""
    show Kimidori Neutral Flip
    "The student council president blinked and looked at his secretary sidelong, obviously very confused."
    nvl clear
    show Kyon Ser2 Flip
    "\"I don't really believe that last part, but it's nice of you to say.\" After a breath, Kyon warned in a low voice, \"I just want to point out, though, that a challenge against any one of us is a challenge against {i}all{/i} of us, so even the entity may have bitten off more than it can chew.\""
    nvl clear
    stop music fadeout 1
    play sound "SE/impact.mp3"
    queue music "Music/Oi.mp3"
    hide Yuki
    hide Mikuru
    hide Koizumi
    show Kyon Ser2 Flip at left
    show Kcut Bandage Flip at left
    hide Kimidori
    #show President at right - Neutral, mouth closed
    with dissolve
    show Haruhi Hips Ang1 at center with moveinleft
    "Before anyone could respond, the door crashed open with a reverberating smash, Haruhi stomping in and taking point in front of Kyon, shooting a dark glare at the president. \"Trying to pick us apart by calling out my underlings when I'm not around, eh?\" she challenged, bristling with fury. \"Well, you've got a lot to learn! A challenge against one of us is a challenge against {i}all{/i} of us!\""
    nvl clear
    show Kyon Smile2 Flip
    show Haruhi Hips Ang2
    "Mikuru blinked, catching Kyon's smirk at the girl in front of him as she echoed his words of only moments before. Emiri's expression had returned to blank neutrality, with small traces of surprise showing as she picked her pen back up and began jotting notes down."
    show Haruhi Hips Ang3
    "\"Really, you are the lowest example of politician!\" Haruhi spat, shaking her head at the president."
    nvl clear
    show Haruhi Hips Ang4
    #show President - Annoyed, mouth closed (with Scary Shiny Glasses, if possible)
    "For his part, the bespectacled boy gave her a cool look, pushing on the bridge of his glasses with two fingers, flashing bright reflective light off them perfectly into Haruhi's eyes as he adjusted the lenses."
    nvl clear
    "He instantly re-assumed his role in Haruhi's presence, his expression gleaming with cold malice. The chief of the SOS Brigade didn't flinch, her angry smile only growing wider."
    show Haruhi Hips Ang3
    "\"Even using underhanded tactics like calling my vice commander in during {i}classes{/i}?\" She paced back and forth shaking her head sadly."
    nvl clear
    "\"I thought you were a rival, maybe someday even an equal, but you're just a sad little man who hides behind whatever political tricks he can to cause trouble for people he doesn't like personally! Trying to make things difficult for Kyon when he defended a fellow student from a crazed pervert?! Don't make me think that Kitago is a school unworthy of its reputation!\""
    show Haruhi Hips Ang4
    nvl clear
    #show President - Angry, narrow eyes
    "\"You overreact,\" the president said in a frosty tone. \"Marching in with your pompous attitude and blatant disregard for policy.... I invite you to check every step of the proceedings of this inquiry; you'll find that each and every one was in complete accordance with official guidelines and policies!"
    nvl clear
    "\"The only breach here is that Kyon-kun was summoned alone. There was no request for Koizumi-kun, Nagato-kun, Asahina-kun, or yourself to be here."
    #show President - Angry, wider mouth
    "\"Really, storming your way into an official meeting that doesn't involve you personally?"
    nvl clear
    "\"This matter has absolutely nothing to do with your so-called club, that unofficial organization that I refuse to acknowledge! This is a personal matter between the student council and a single student. Your show of force is both unseemly and needlessly exaggerated.\""
    nvl clear
    show Haruhi Hips Ang1
    #show President - Angry, closed mouth
    "\"Ooh!\" Haruhi exclaimed, standing still to stomp one foot on the floor and shoot a murderous glare at the president. \"Nice try,\" she retorted with a sneer, \"but if it smells like a load of crap, looks like a load of crap, and acts like a load of crap ... then it's a {i}load of crap{/i}!"
    nvl clear
    "\"One of my brigade members was attacked by a crazed student! Another of my brigade members did his civic duty not only as a member of the brigade you don't acknowledge, but as a {i}citizen{/i}! An upstanding {i}student{/i} of this school!"
    nvl clear
    show Haruhi Hips Ang3
    "\"You're all high-and-mighty behind your desk, proud of the fact that you get to pick on my crew just because you don't like them! What about all the other students who just {i}watched{/i} a crazed upperclassman with a {i}knife{/i} haul away a defenseless first year student? Not one of {i}them{/i} is worthy of reprimand?\""
    nvl clear
    show Haruhi Hips Ang4
    #show President - Angry, tightly closed mouth (with Scary Shiny Glasses, if possible)
    "The president's face was a mask of contempt and barely concealed rage. He slowly lowered his head, allowing the mirror-bright shine of his glasses to reflect to the floor and his eyes to become visible. "
    #show President - Angry, teeth clenched
    extend "\"Very well,\" he grated out, in the tone of someone who was having a tooth pulled without anesthetic."
    nvl clear
    "\"In light of the greater failing of the student populous in general, we will dismiss the {i}gross{/i} disciplinary issues in Kyon-kun's behavior ... {i}this{/i} time. After all, my quarrel isn't with your underlings, but you. Now leave, Suzumiya-kun, before my good graces run out.\""
    nvl clear
    scene bg ClubHallRight with fade
    show Mikuru Cower Sigh1 at right with dissolve
    "Haruhi allowed herself a single imperious sniff before turning on her heel and grabbing Kyon's hand, hauling him out of the room. Mikuru hesitated, walking in step with Yuki when she finally left, though the shorter girl's eyes had been fixed on Emiri the entire time.{w} Once they were in the hall, the time traveler released a shaky, explosive sigh. \"Scary,\" Mikuru moaned. \"And now we're late for class!\""
    nvl clear    
    show Mikuru Cower Sigh2
    show Haruhi Hap1 at left with dissolve
    "\"No problem, no problem!\" Haruhi said brightly, seeming charged with her victory over the student council president. \"Tell your teachers to take their complaints to the student council! They hauled us out of class for this, after all.\"{p}Turning to Kyon, she added in a more serious tone, \"You need to be careful, Kyon! I can't always bail you out when you get into trouble like this! And you owe Koizumi-kun a thanks for texting me that this was even happening!\""
    nvl clear
    show Haruhi Smile3
    show Kyon Smile3 at center 
    show Kcut Bandage at center
    with dissolve
    "\"Oh, yeah? Thanks, Koizumi, glad you're so on-the-ball.\" The esper maintained his eternal smile, nodding slightly. \"Anyway, Haruhi, would you be mad at me if I was confident enough in you to say that you could bail me out again?\" Kyon asked her."
    nvl clear    
    show Kyon Smile2
    show Haruhi Sup1
    show Mikuru Quest2
    "Haruhi made a squeaking noise and dropped Kyon's hand\nas if burned, her face turning pink. {nw}"
    show Hblush at left
    show Haruhi Pout2
    show Mikuru Neutral2
    extend "\"W...well, that may be the case!\" she allowed, nodding and looking away. \"But, just because I can pick up the pieces doesn't mean you should rely on that!\""
    nvl clear    
    show Haruhi Pout1
    show Kyon Smile6
    "He gave her a weak grin. \"Sorry, but I may have to a bit before this investigation finishes,\" he said apologetically. \"Um, but I'll talk with Tsuruya-kun — she probably won't mind letting you take our final report to the student council president. Trust me, that'll be a {i}huge{/i} bargaining chip to use against him.\""
    nvl clear
    hide Hblush
    show Kyon Smile1
    show Haruhi Sigh2
    "\"Bah!\" Haruhi groused, as they entered the walkway to the second year classes. \"I don't like that at all! I didn't do any work, and I don't even know what it's about! How am I supposed to use that?\""
    show Haruhi Unhap3
    show Kyon Neutral2
    "\"It's something completed entirely by your vice commander and an honorary member,\" Kyon assured her. \"That makes it a part of the SOS Brigade, doesn't it?\""
    nvl clear
    show Kyon Neutral3
    show Haruhi Quest1
    "\"Oh, well, I suppose that's true....\""
    show Haruhi Quest2
    show Mikuru Smile2
    "Mikuru smiled, shaking her head {nw}"
    $ _window = True
    hide Mikuru with moveoutright
    $ _window = False
    extend "and waving as she turned to take the walkway to the third year classes."
    nvl clear
    show Kyon Smile4
    "Kyon caught the wave and gave her a grin, waving back before turning to face Haruhi. Even though she had no idea what Kyon had needed to travel to yesterday for, she was glad she could help with it. And she couldn't help but feel glad when he had said that the brigade was a team, and no single one of them could be attacked without the others. Maybe, she decided, she was a greater asset than she had let herself believe previously."
    nvl clear
    "Cheered by that thought, she was able to smile when she entered her classroom and apologetically informed the teacher she was late due to student council business."
    nvl clear
    stop music fadeout 3
    
    call eyecatch_fancy("Thursday, April 21") from HAB1_sc003
    
    queue music "Music/Nanika.mp3"
    scene bg classroom with fade:
       size (800,600)
    "During the next break after lunch, Haruhi pulled the half-eaten bento from her schoolbag and wordlessly poked Kyon in the back with it. He turned and accepted it with a raised eyebrow. \"I'm really lucky to have such a considerate brigade chief looking out for me,\" he said, before she could point it out for him."
    "She tried to scowl, but could only manage a knowing smirk. \"You'd better believe it!\" she told him, nodding studiously. \"Oh, did you finish your math homework?\""
    nvl clear
    show Kunikida Neutral1 at TenthRight
    show Taniguchi Grin1 at left
    with dissolve
    "\"Barely,\" he allowed, before digging into the bento. Haruhi wasn't at all surprised when Taniguchi and Kunikida rose to approach Kyon, and evidently he expected it as well, since he just grunted wordlessly before polishing off the bento and asking, \"What this time?\""
    show Kunikida Neutral2
    "\"Ah ... well,\" Kunikida temporized, chuckling guiltily, \"I wanted to apologize to you, Kyon ... it wasn't right to make those judgments.\""
    nvl clear
    show Kunikida Neutral1
    show Taniguchi Hap2
    "\"Mostly, I just wanted to ask when you took a level of badass,\" Taniguchi contributed. \"And to tell you I'm a bit jealous of you getting yet another A minus into your club. Mega points for saving her bacon from the jerk — a few more stunts like that and you're going to have your own fanclub!\""
    show Taniguchi Grin1
    "\"'A minus'?\" Haruhi echoed, frowning. \"What's that mean?\""
    nvl clear
    "\"Eh,\" Kyon sighed, shaking his head. \"Taniguchi's a living perv-wiki. He's rated all the girls on a grading scale and only learns the names of those who get an 'A' or better.\""
    show Taniguchi Ser2
    "\"Well, I know where I must stand on that scale,\" Haruhi allowed, shooting Taniguchi a sharp glance. \"Which is funny, because on my scale, Taniguchi isn't quite rated fifteen minutes.\""
    nvl clear
    show Taniguchi Unhap1
    "Taniguchi grimaced. {nw}"
    show Taniguchi Ser3
    extend "\"Nevermind that!\" he protested. \"This is about Kyon the delinquent and his rise to school celebrity!\""
    show Taniguchi Ser2
    "\"That's great,\" Kyon returned. \"Because I don't care to discuss it. I already had to explain my situation to the student council, and Ryuguu's getting expelled. As far as I'm concerned, it's a closed issue.\""
    nvl clear
    show Kunikida Smile2
    "\"Yes, but he cut you and you don't even seem to care,\" Kunikida said, grinning. \"It's hard not to be a bit in awe, you know?\""
    show Kunikida Smile1
    "\"I'm sure you can find any number of rumor-mongers who are willing to tell you whatever you want to hear,\" Kyon replied."
    nvl clear
    "\"Yeah, I hear Yanagimoto's got a bunch of them to trade,\" Haruhi added. \"Of course, it's really hard to believe any of them for me, but if you want baseless rumors, go nuts....\""
    show Taniguchi Hap2
    "\"Will do!\" Taniguchi said cheerfully. \"A 'B-plus' isn't too far off from an 'A-minus'!\" Turning around, he stepped over to Yanagimoto's desk and immediately tried to strike up a conversation."
    hide Taniguchi with dissolve
    "\"Sometimes, I worry about that guy,\" Kyon said, shaking his head."
    nvl clear
    "Haruhi thought about it for a minute, then said, \"I don't think his chronic stupidity is likely to hurt him too badly. And it's not like he could get {i}dumber{/i}.\""
    show Kunikida Smile2
    "\"Aha ... well ... I'll leave you two to be, then,\" Kunikida decided, drawing away with a short bow."
    hide Kunikida with dissolve
    "\"But, hey, how about that, Kyon? You're a school celebrity! This is going to be {i}great{/i} publicity for the brigade! Man, if only you'd aspired to become vice commander sooner!\""
    nvl clear
    "\"Yeah, it's gonna be great fun talking to my parents about that tonight,\" Kyon agreed, grimacing."
    "Haruhi snapped her fingers decisively. \"I'll go with you and we can bring Kanae-chan,\" she declared. \"This is big, so we can skip the club meeting for today. Problem solved! Unless your parents are aliens or worse, there's no way they could hear her explanation for what happened with her extra-moe face and speech without giving in! It's a tiny bit annoying, but that worshipful 'Sempai' of hers is guaranteed to melt the hearts of anyone!\""
    nvl clear
    "\"Yeah ... I guess,\" he allowed, nodding. \"Feels a bit weak to always be relying on girls to take care of my problems for me.\""
    "\"Oh, like the way you hid behind Kanae-chan in your fight earlier?\" she giggled. \"Or the way you meekly hid behind Tsuruya while she fought off a dozen Yakuza?\""
    "\"Hmm,\" Kyon mused, handing the empty bento back to her. \"That's a good point! Thanks, Haruhi.\""
    "She nodded, catching another gesture from Sakanaka and turning her head in time to see the other girl wink at her and make a small 'victory' sign. Haruhi couldn't help but grin at her friend and return the sign."
    nvl clear
    stop music fadeout 3
    
    jump HAB2
