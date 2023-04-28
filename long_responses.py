import random
R_EATING = 'I don\'t like eating anything because im a bot obviously'
GMACIC = 'Sure:' \
       '\n#include<stdio.h>' \
       '\nint main(){' \
       '\nint num;' \
       '\nprintf("Welcome to AI Code")' \
       '\nprintf("enter num:")' \
       '\nscanf("%d",&num)' \
       '\nprintf("%d",num)' \
       '\nreturn 0;' \
       '\n}'
HWAM = "Windows are made by cutting, cleaning, sealing, and assembling glass and frames.\n" \
       " There are different types of windows, such as wooden windows1 or glass windows2, \n" \
       "that may have different materials and processes involved. For example,\n" \
       " glass windows are produced by mixing and melting soda, sand, ash, limestone, dolomite, and salt cake at high temperatures2.\n" \
       " Wooden windows are made by cutting and shaping wood pieces and fitting them with glass panes"
IDLTS = "please enter the problem by typing  /prob is: ...   "

# PROBLEMS---------------------------------------------------------------------------------------------------
ToSlow = 'That is a Problem i can\'t solve please contact the developer'
givwrongres = 'that is being solved by the develeper its a matter of best match\n please type more accurate keywords for me to answer you as the problem is being fixed'
randbigwords = 'that is a leak in the code that shows how well the words you typed matches with my responses'
failtoop = 'that is being fixed by the developer its a matter of wrong words i.e  \n\nYou:sdjhabsd\n\n please avoid typing errors as the problem is being fixed'
# PROBLEMS----------------------------------------------------------------------------------------------------


def unknown():
    response = ["Could you please re-phrase that?",
                "..."
                'Sounds about right'
                "what does that mean?"]
    [random.randrange(4)]
    return response
