#SimpZone
'''Hello, it appears that you have found
   a program to diagnose any simp tendencies.'''
   
#imports
import numpy as nms 
import random 
import sys 
import time 

#class_[color_method]
class color_method:
    
    #def_[RED]
    def RED(string):
        red ='\033[91m'
        return red +str(string)
        
    #def_[YELLOW]
    def YELLOW(string):
        yellow ='\033[93m'
        return yellow +str(string)
        
    #def_[WHITE]
    def WHITE(string):
        white ='\033[97m'
        return white +str(string)
        
#banner
def banner():
    print(color_method.YELLOW('''
███████╗██╗███╗   ███╗██████╗ ███████╗ ██████╗ ███╗   ██╗███████╗ 
██╔════╝██║████╗ ████║██╔══██╗╚══███╔╝██╔═══██╗████╗  ██║██╔════╝ 
███████╗██║██╔████╔██║██████╔╝  ███╔╝ ██║   ██║██╔██╗ ██║█████╗   
╚════██║██║██║╚██╔╝██║██╔═══╝  ███╔╝  ██║   ██║██║╚██╗██║██╔══╝   
███████║██║██║ ╚═╝ ██║██║     ███████╗╚██████╔╝██║ ╚████║███████╗ 
╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ 
                                                                  
██████╗ ██╗ █████╗  ██████╗ ███╗   ██╗ ██████╗ ███████╗██╗███████╗
██╔══██╗██║██╔══██╗██╔════╝ ████╗  ██║██╔═══██╗██╔════╝██║██╔════╝
██║  ██║██║███████║██║  ███╗██╔██╗ ██║██║   ██║███████╗██║███████╗
██║  ██║██║██╔══██║██║   ██║██║╚██╗██║██║   ██║╚════██║██║╚════██║
██████╔╝██║██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝███████║██║███████║
╚═════╝ ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝╚══════╝
                                                                  
    '''))
    print(color_method.WHITE('made_by: ') +color_method.RED('None'))
    print(color_method.WHITE('version: ') +color_method.RED('[1.0]'))
    print(color_method.WHITE('support: ') +color_method.RED('Simp//incel//doomer//NPC'))
    print(color_method.WHITE('built_with: ') +color_method.RED('Python_[3.8.3]'))

#class_[simp_diagnosis_tool]
class simp_diagnosis_tool:
    
    #self
    def __init__(self):
        self.name = str(input(color_method.RED('enter name for diagnosis: ')))
        #questions
        print('\nsection [1]')
        print('answer with: [1==YES] <> [0==NO]')
        #simp_inputs
        self.simp1 = int(input(color_method.RED('\ndo you think you are currently a simp: ')))
        self.simp2 = int(input('do your freinds accuse you of being a simp: '))
        self.simp3 = int(input('have you had any acts of simping in the past: '))
        self.simp4 = int(input('you have never had a girlfreind: '))
        self.simp5 = int(input('you have been rejected by a whamen/boi: '))
        self.simp6 = int(input('you have been rejected multiple times by the same person: '))
        self.simp7 = int(input('you activly try to get girls to like you: '))
        self.simp8 = int(input('you have been dumped before: '))
        self.simp9 = int(input('you are a liberal: '))
        self.simp10 = int(input('your life is dependant on chasing whamen/bois: '))
        self.simp11 = int(input('you despise slander of any female: '))
        self.simp12 = int(input('you desperatly try to promote feminism no matter how many flaws it exibhits: '))
        self.simp13 = int(input('you had a crush for 2 years: '))
        self.simp14 = int(input('you had a crush for 3 years: '))
        self.simp15 = int(input('you had a crush for 4 years: '))
        self.simp16 = int(input('you had a crush for 5++ years: '))
        self.simp17 = int(input('you have spent money trying to get whamen/bois to like you: '))
        self.simp18 = int(input('you have been to more than 3 dances in a year to get a date: '))
        self.simp19 = int(input('you let people walk over you: '))
        self.simp20 = int(input('you resist change: '))
        #incel_inputs
        print('\nsection [2]')
        print('answer with: [1==YES] <> [0==NO]')
        self.incel1 = int(input('do you identify as a involintary celibate [incel]: '))
        self.incel2 = int(input('are you an incel by textbook/dictionary definition: '))
        self.incel3 = int(input('are you unable to sympathise with popular people: '))
        self.incel4 = int(input('do you dislike chads: '))
        self.incel5 = int(input('do you feel unable to connect with others: '))
        self.incel6 = int(input('do you have a sense that you are better than most others: '))
        self.incel7 = int(input('do others describe you as entitled: '))
        self.incel8 = int(input('do others around you think you are an incel: '))
        self.incel9 = int(input('do members of the opposite gender resent your precence: '))
        self.incel10 = int(input('do you use 4chan: '))
        self.incel11 = int(input('are you part of any toxic subreddits: '))
        self.incel12 = int(input('do you think that one particular gender is better than the other[s]: '))
        self.incel13 = int(input('are you by definition as sexist: '))
        self.incel14 = int(input('do you feel entitled to a relationship: '))
        self.incel15 = int(input('do you resent chads: '))
        self.incel16 = int(input('do you actively preach absinence: '))
        self.incel17 = int(input('do you blame others for celibacy in the world: '))
        self.incel18 = int(input('do you think that others are inferior to yourself: '))
        self.incel19 = int(input('do you look down on stacys [female version of chads]: '))
        self.incel20 = int(input('are you a narcissist by textbook/dictionary definition: '))
        #doomer_inputs
        print('\nsection [3]')
        print('answer with: [1==YES] <> [0==NO]')
        self.doomer1 = int(input('do you think you are a doomer: '))
        self.doomer2 = int(input('do you think the survival of humanity is based on race: '))
        self.doomer3 = int(input('do you believe that immigration will be the downfall of humanity: '))
        self.doomer4 = int(input('are you active on 4chan: '))
        self.doomer5 = int(input('are you active in political subdomains of twitter: '))
        self.doomer6 = int(input('do you support race based politics: '))
        self.doomer7 = int(input('do you think that society is against people like you: '))
        self.doomer8 = int(input('do you think society is to blame for your state in life: '))
        self.doomer9 = int(input('do you consider yourself an intellectual: '))
        self.doomer10 = int(input('are you a supporter of 3rd party campaigns: '))
        self.doomer11 = int(input('do you find the government to be corrupt:'))
        self.doomer12 = int(input('does society hold unreallistic standards: '))
        self.doomer13 = int(input('do you think the economy is rigged: '))
        self.doomer14 = int(input('do you find most sucessful people apathetic for the ones struggling: '))
        self.doomer15 = int(input('do you think that general apathy will be lead to our downfall: '))
        self.doomer16 = int(input('do you have conspiracy against the government: '))
        self.doomer17 = int(input('do you belive the government is immoral and corrupt: '))
        self.doomer18 = int(input('do you find most others in society to be oblivious and incompitent'))
        self.doomer19 = int(input('do your freinds find your political stance extreme: '))
        self.doomer20 = int(input('do you have non-mainstream veiws on most issues: '))
        #NPC_input
        print('\nsection [4]')
        print('anwser with: [1==YES] <> [0==NO]')
        self.NPC1 = int(input('are you on the political left: '))
        self.NPC2 = int(input('do you belive that the government should have full control: '))
        self.NPC3 = int(input('do your freinds call you an NPC: '))
        self.NPC4 = int(input('do you think you are an NPC: '))
        self.NPC5 = int(input('if you are on the left, are you mainstream [if on the right, say no]: '))
        self.NPC6 = int(input('are you a bad leader: '))
        self.NPC7 = int(input('do you let others lead projects: '))
        self.NPC8 = int(input('do you believe that some are people are just natural leaders: '))
        self.NPC9 = int(input('do you not question the government: '))
        self.NPC10 = int(input('do you only rely on a single news source: '))
        self.NPC11 = int(input('is your political stance the same as that of your parents: '))
        self.NPC12 = int(input('have you been called out for being an NPC on twitter: '))
        self.NPC13 = int(input('do you recieve a lot of hate on 4chan: '))
        self.NPC14 = int(input('do you always side with the more powerful person: '))
        self.NPC15 = int(input('are you willing to seek change in politics: '))
        self.NPC16 = int(input('do you need others to guide your opinion: '))
        self.NPC17 = int(input('do you struggle to think for yourself: '))
        self.NPC18 = int(input('do people think of you as unintelligent: '))
        self.NPC19 = int(input('do you have trouble identifying bias: '))
        self.NPC20 = int(input('are you weak in defending your argument in debate: '))
        
    #def_[simp_syntax]
    def simp_syntax(self):
        #simp_array
        simp_array = nms.array(
            [[self.simp1, self.simp2, self.simp3, self.simp4, self.simp5, self.simp6, self.simp7, self.simp8, self.simp9, self.simp10],
            [self.simp11, self.simp12, self.simp13, self.simp14, self.simp15, self.simp16, self.simp17, self.simp18, self.simp19, self.simp20]]
            )
        #simp_score
        simp_score = (
            self.simp1+ self.simp2+ self.simp3+ self.simp4+ self.simp5+ self.simp6+ self.simp7+ self.simp8+ self.simp9+ self.simp10+
            self.simp11+ self.simp12+ self.simp13+ self.simp14+ self.simp15+ self.simp16+ self.simp17+ self.simp18+ self.simp19+ self.simp20
            )
        #try_exception_block
        try:
            #ifs_elifs_else
            if int(simp_score) > int(15):
                print(color_method.YELLOW('\ndiagnosis: simp'))
                print('simp score: {}'.format(simp_score))
                print('simp array: ')
                print(simp_array)
            elif int(simp_score) > int(10) and int(simp_score) < int(16):
                print('\ndiagnosis: simp tendencies [high]')
                print('simp score: {}'.format(simp_score))
                print('simp array: ')
                print(simp_array)
            elif int(simp_score) > int(5) and int(simp_score) < int(11):
                print('\ndiagnosis: simp tendencies [low]')
                print('simp score: {}'.format(simp_score))
                print('simp array: ')
                print(simp_array)
            elif int(simp_score) < int(6):
                print('\ndiagnosis: not a simp')
                print('simp score: {}'.format(simp_score))
                print('simp array: ')
                print(simp_array)
            else:
                print('\ninvalid input: try again')
                time.sleep(5)
                sys.exit(1)
        #exeptions
        except Exception as ERR:
            print('error: {}'.format(ERR))
            
    #def_[incel_syntax]
    def incel_syntax(self):
        #simp_array
        incel_array = nms.array(
            [[self.incel1, self.incel2, self.incel3, self.incel4, self.incel5, self.incel6, self.incel7, self.incel8, self.incel9, self.incel10],
            [self.incel11, self.incel12, self.incel13, self.incel14, self.incel15, self.incel16, self.incel17, self.incel18, self.incel19, self.incel20]]
            )
        #simp_score
        incel_score = (
            self.incel1+ self.incel2+ self.incel3+ self.incel4+ self.incel5+ self.incel6+ self.incel7+ self.incel8+ self.incel9+ self.incel10+
            self.incel11+ self.incel12+ self.incel13+ self.incel14+ self.incel15+ self.incel16+ self.incel17+ self.incel18+ self.incel19+ self.incel20
            )
        #try_exception_block
        try:
            #ifs_elifs_else
            if int(incel_score) > int(15):
                print(color_method.YELLOW('\ndiagnosis: incel'))
                print('incel score: {}'.format(incel_score))
                print('incel array: ')
                print(incel_array)
            elif int(incel_score) > int(10) and int(incel_score) < int(16):
                print('\ndiagnosis: incel tendencies [high]')
                print('incel score: {}'.format(incel_score))
                print('incel array: ')
                print(incel_array)
            elif int(incel_score) > int(5) and int(incel_score) < int(11):
                print('\ndiagnosis: incel tendencies [low]')
                print('incel score: {}'.format(incel_score))
                print('incel array: ')
                print(incel_array)
            elif int(incel_score) < int(6):
                print('\ndiagnosis: not an incel')
                print('incel score: {}'.format(incel_score))
                print('incel array: ')
                print(incel_array)
            else:
                print('\ninvalid input: try again')
                time.sleep(5)
                sys.exit(1)
        #exeptions
        except Exception as ERR:
            print('error: {}'.format(ERR))
            
        #def_[incel_syntax]
    def NPC_syntax(self):
        #simp_array
        NPC_array = nms.array(
            [[self.NPC1, self.NPC2, self.NPC3, self.NPC4, self.NPC5, self.NPC6, self.NPC7, self.NPC8, self.NPC9, self.NPC10],
            [self.NPC11, self.NPC12, self.NPC13, self.NPC14, self.NPC15, self.NPC16, self.NPC17, self.NPC18, self.NPC19, self.NPC20]]
            )
        #simp_score
        NPC_score = (
            self.NPC1+ self.NPC2+ self.NPC3+ self.NPC4+ self.NPC5+ self.NPC6+ self.NPC7+ self.NPC8+ self.NPC9+ self.NPC10+
            self.NPC11+ self.NPC12+ self.NPC13+ self.NPC14+ self.NPC15+ self.NPC16+ self.NPC17+ self.NPC18+ self.NPC19+ self.NPC20
            )
        #try_exception_block
        try:
            #ifs_elifs_else
            if int(NPC_score) > int(15):
                print(color_method.YELLOW('\ndiagnosis: NPC'))
                print('NPC score: {}'.format(NPC_score))
                print('NPC array: ')
                print(NPC_array)
            elif int(NPC_score) > int(10) and int(NPC_score) < int(16):
                print('\ndiagnosis: NPC tendencies [high]')
                print('NPC score: {}'.format(NPC_score))
                print('NPC array: ')
                print(NPC_array)
            elif int(NPC_score) > int(5) and int(NPC_score) < int(11):
                print('\ndiagnosis: NPC tendencies [low]')
                print('NPC score: {}'.format(NPC_score))
                print('NPC array: ')
                print(NPC_array)
            elif int(NPC_score) < int(6):
                print('\ndiagnosis: not an NPC')
                print('NPC score: {}'.format(NPC_score))
                print('NPC array: ')
                print(NPC_array)
            else:
                print('\ninvalid input: try again')
                time.sleep(5)
                sys.exit(1)
        #exeptions
        except Exception as ERR:
            print('error: {}'.format(ERR))
            
           #def_[doomer_syntax]
    def doomer_syntax(self):
        #simp_array
        doomer_array = nms.array([[
            self.doomer1, self.doomer2, self.doomer3, self.doomer4, self.doomer5, self.doomer6, self.doomer7, self.doomer8, self.doomer9, self.doomer10],
            [self.doomer11, self.doomer12, self.doomer13, self.doomer14, self.doomer15, self.doomer16, self.doomer17, self.doomer18, self.doomer19, self.doomer20
            ]])
        #doomer_score
        doomer_score = (
            self.doomer1+ self.doomer2+ self.doomer3+ self.doomer4+ self.doomer5+ self.doomer6+ self.doomer7+ self.doomer8+ self.doomer9+ self.doomer10+
            self.doomer11+ self.doomer12+ self.doomer13+ self.doomer14+ self.doomer15+ self.doomer16+ self.doomer17+ self.doomer18+ self.doomer19+ self.doomer20
            )
        #try_exception_block
        try:
            #ifs_elifs_else
            if int(doomer_score) > int(15):
                print(color_method.YELLOW('\ndiagnosis: doomer'))
                print('doomer score: {}'.format(doomer_score))
                print('doomer array: ')
                print(doomer_array)
            elif int(doomer_score) > int(10) and int(doomer_score) < int(16):
                print('\ndiagnosis: doomer tendencies [high]')
                print('doomer score: {}'.format(doomer_score))
                print('NPC array: ')
                print(doomer_array)
            elif int(doomer_score) > int(5) and int(doomer_score) < int(11):
                print('\ndiagnosis: doomer tendencies [low]')
                print('doomer score: {}'.format(doomer_score))
                print('doomer array: ')
                print(doomer_array)
            elif int(doomer_score) < int(6):
                print('\ndiagnosis: not a doomer')
                print('doomer score: {}'.format(doomer_score))
                print('doomer array: ')
                print(doomer_array)
            else:
                print('\ninvalid input: try again')
                time.sleep(5)
                sys.exit(1)
        #exeptions
        except Exception as ERR:
            print('error: {}'.format(ERR))
            
#def_[conditions_and_future_development]
def conditions_and_future_development():
    print(color_method.WHITE('''
\nSIMP: Noun. simp (plural simps) (slang) A simple person lacking common sense;
a fool or simpleton.(slang) A man who foolishly overvalues a woman and puts her
on a pedestal.
      
INCEL: The term "involuntary celibate" (shortened to "incel") refers to self-identifying
members of an online subculture based around the inability to find a romantic
or sexual partner despite desiring one, a state they describe as "inceldom" or "incelibacy". 
     
CHAD: Incels see women as either “Stacys,” who are hyperfeminine, attractive, and
unattainable and who only date “Chads”(muscular, popular men who are presumed to sleep
with lots of women), or “Beckys,” the “average” woman.  
      
DOOMER: A doomer is someone who believes that global problems—including but not limited to
ecological exhaustion, such as overpopulation, peak oil, climate change, and
pollution—will cause the collapse of civilization, significant human population die-off,
and potentially lead to eventual human extinction.
      
NPC: NPC, derived from Non-Player Character in video games, is an Internet meme that expresses
the idea that individuals on the political left do not think for themselves; it is also
known as NPC [IN4].

THOT: A man/woman who has many casual sexual encounters or relationships.

MAN HOE: A guy that will date many girls at once or a guy that will talk to many girls at one time.

STACY//TRIXIE: The female counterpart to the Chad, in slang, is the Trixie or the Stacy.
These people often take part in the same activities of and spend time with the Chads. the
incels dislike them because they can't get them.

PEDOOMER: A pedo. Plain and simple. Will probably go to jail for
creeping on an underage person and will most likely get caught on True Crime Daily
by Chris Hansen.

COOMER: You don't want to know. Just google it if you REALLY want to find out.

E-GIRL: E-girls are a subculture derived from social media platforms like TikTok and Instagram and
are typically categorized by winged eyeliner, vibrant and heavy eyeshadow, and a child-like
aesthetic often associated with anime, cosplay, and other acts of thottery.

E-BOY: The male version of the E-girl. Arguably worse on average.

VSCO GIRL: High school subcultural dynamics are explored and consumed by people a decade or
more removed from them. Teenagers, particularly teenage girls, have long been the
subject of fascination for adults, and the VSCO girl, whose name comes from the photo-editing app 
(pronunciation: “visco”) is only the latest iteration of how we express it. These creatures
are often seen with 80$ hydroflasks, stupid t-shirts, scrunchies, and are often identified
because they're always saying sksksksksksksksksksks.

VSCO BOY: Pretty much the same as a VSCO girl. Most of the time they're even more
irritating.

WARNING_B: This dev only diagnoses SIMP, DOOMER, INCEL and NPC. Updates coming soon.
    '''))

#if_[name==main]
if __name__ ==str('__main__'):
    banner()
    ask =int(input('do you want to see the condition dictionary [1==yes] <> [0==no]: '))
    
    #ifs_elifs_else
    if bool(ask) is True:
        conditions_and_future_development()
    else:
        pass
    
    simp_zones = simp_diagnosis_tool()
    #call_functions
    simp_zones.simp_syntax()
    simp_zones.incel_syntax()
    simp_zones.NPC_syntax()
    simp_zones.doomer_syntax()
    END_CARD =str(input())
else:
    print(' ')

                                
