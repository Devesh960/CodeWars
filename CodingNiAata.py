from math import *
import random
import ast

name = "CodingNiAata"

def circle(pirate):
    target = Pirate_list(pirate)
    target[4] = -target[4]
    target[4] = target[4]%17
    if(target[4]<=4):
        target[4]+=1
        target[4] = -target[4]
        Pirate_list(pirate,target)
        return 2
    
    elif(target[4]<=8):
        target[4]+=1
        target[4] = -target[4]
        Pirate_list(pirate,target)
        return 3
    
    elif(target[4]<=12):
        target[4]+=1
        target[4] = -target[4]
        Pirate_list(pirate,target)
        return 4
    
    elif(target[4]<=15):
        target[4]+=1
        target[4] = -target[4]
        Pirate_list(pirate,target)
        return 1
    
    elif(target[4]==16):
        target[4] = 1
        target[4] = -target[4]
        Pirate_list(pirate,target)
        return 1

def gandmasti(pirate,x,y):
    forbidden = pirate.getDeployPoint()
    current_position = pirate.getPosition()
    X = pirate.getDimensionX()
    Y = pirate.getDimensionY()
    l = Pirate_list(pirate) 
    s = l[3]
    move_list = [[X/10,1],[1,Y/10],[2*X/10,1],[1,2*Y/10],[3*X/10,1],[1,3*Y/10],[4*X/10,1],[1,4*Y/10],[5*X/10,1],[1,5*Y/10],[6*X/10,1],[1,6*Y/10],[7*X/10,1],[1,7*Y/10],[8*X/10,1],[1,8*Y/10],[9*X/10,1],[1,9*Y/10],[X-1,1],[1,Y-1],[X-1,Y/10],[X/10,Y-1],[X-1,2*Y/10],[2*X/10,Y-1],[X-1,3*Y/10],[3*X/10,Y-1],[X-1,4*Y/10],[4*X/10,Y-1],[X-1,5*Y/10],[5*X/10,Y-1],[X-1,6*Y/10],[6*X/10,Y-1],[X-1,7*Y/10],[7*X/10,Y-1],[X-1,8*Y/10],[8*X/10,Y-1],[X-1,9*Y/10],[9*X/10,Y-1],[X-1,Y-1]] 
    m=[]
    if type(s)!= int :
        m =  ast.literal_eval(s[:-1])
    if l[3]==4:
        l[3]=f"[{x},{y}]1"
        Pirate_list(pirate,l)
        return 0
    elif s[-1]=="1" and current_position != (x,y) :
        return moveTo(x,y,pirate)
    elif s[-1]=="1" and current_position == (x,y) :
        r = random.randint(0,38)
        t = move_list[r]
        s = f"{t}2"
        l[3] = s
        Pirate_list(pirate,l)
        return 0
    elif s[-1]=="2" and current_position!=(m[0],m[1]):
        return moveTo(m[0],m[1],pirate)
    elif s[-1]=="2" and current_position==(m[0],m[1]):
        l[3] = f"[{x},{y}]1"
        Pirate_list(pirate,l)
        return 0

def random_move(pirate,x,y,n): #x and y denote the islands co ordinates
    commands = "ulddrruuldurddlluurddruullddrudluurrddlurdlluurrdlrullddrrullurrddllurldrruulldr"
    l = Pirate_list(pirate)
    counter = l[n]
    if pirate.getPosition()!=(x,y) and counter==0:
        return moveTo(x,y,pirate)
    else: 
        current_command = commands[counter%80]
        l[n] += 1
        Pirate_list(pirate,l)
        if current_command=="u":
            return 1
        elif current_command=="r":
            return 2
        elif current_command=="d":
            return 3
        elif current_command=="l":
            return 4

def island(pirate,n):
    team = Team_list(pirate)
    target = Pirate_list(pirate)
    count = team[n+9]%17
    if(count==0):
        target.append(count)
        target.append(n)
        target[0] = team[3+2*(n-1)+1]
        target[1] = team[3+2*(n-1)+2]
        Pirate_list(pirate,target)
        team[n+9]+=1
        Team_list(pirate,team)
        return moveTo(team[3+2*(n-1)+1],team[3+2*(n-1)+2],pirate)
    
    elif(count<=4):
        target.append(count)
        target.append(n)
        target[0] = team[3+2*(n-1)+1] + count - 3
        target[1] = team[3+2*(n-1)+2] - 2
        Pirate_list(pirate,target)
        team[n+9]+=1
        Team_list(pirate,team)
        return moveTo(team[3+2*(n-1)+1] + count- 3,team[3+2*(n-1)+2]-2,pirate)
    
    elif(count<=8):
        target.append(count)
        target.append(n)
        target[0] = team[3+2*(n-1)+1] + 2
        target[1] = team[3+2*(n-1)+2] + count - 7
        Pirate_list(pirate,target)
        team[n+9]+=1
        Team_list(pirate,team)
        return moveTo(team[3+2*(n-1)+1] - count + 7,team[3+2*(n-1)+2]+2,pirate)
    
    elif(count<=12):
        target.append(count)
        target.append(n)
        target[0] = team[3+2*(n-1)+1] - count + 11
        target[1] = team[3+2*(n-1)+2] + 2
        Pirate_list(pirate,target)
        team[n+9]+=1
        Team_list(pirate,team)
        return moveTo(team[3+2*(n-1)+1]-2,team[3+2*(n-1)+2] + count - 11,pirate)
    
    elif(count<=16):
        target.append(count)
        target.append(n)
        target[0] = team[3+2*(n-1)+1] - 2
        target[1] = team[3+2*(n-1)+2] - count + 15
        Pirate_list(pirate,target)
        team[n+9]+=1
        Team_list(pirate,team)
        return moveTo(team[3+2*(n-1)+1]+2,team[3+2*(n-1)+2] - count + 15,pirate)
        
def Team_list(pirate,l="n"):
    if l=="n":
        a = pirate.getTeamSignal()
        a = ast.literal_eval(a)
        return a   
    else:
        a =f"{l}"
        pirate.setTeamSignal(a)
        
def Pirate_list(pirate,l="n"):
    if l=="n":
        a = pirate.getSignal()
        a = ast.literal_eval(a)
        return a   
    else:
        a =f"{l}"
        pirate.setSignal(a)
        


def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1
    
def start(pirate,deploy,X,Y):
    
    sig = Team_list(pirate)
    
    count = sig[0]%X
    
    if(deploy == (0,Y-1)):
        
        if (count%2==0):
            if(count==0):
                s = [0,0,count/2,1]
                Pirate_list(pirate,s)
                sig[0] +=1
                Team_list(pirate,sig)
                return moveTo(0,0,pirate)
            else:
                s = [count/2,Y-1,count/2,1]
                Pirate_list(pirate,s)
                sig[0] +=1
                Team_list(pirate,sig)
                return moveTo(count/2,Y-1,pirate)
        else:
            if(count==1):
                s = [X-1,Y-1,(count-1)/2,0]
                Pirate_list(pirate,s)
                sig[0] +=1
                Team_list(pirate,sig)
                return moveTo(X-1,Y-1,pirate)
            else:
                s = [0,Y-1-(count-1)/2,(count-1)/2,0]
                Pirate_list(pirate,s)
                sig[0] +=1
                Team_list(pirate,sig)
                return moveTo(0,Y-1-(count-1)/2,pirate)
            
    elif(deploy == (0,0)):
        
        if (count%2==0):
            if(count==0):
                s = [0,Y-1,count/2,1]
                Pirate_list(pirate,s)
                sig[0] +=1
                Team_list(pirate,sig)
                return moveTo(0,Y-1,pirate)
            else:
                s = [count/2,0,count/2,1]
                Pirate_list(pirate,s)
                sig[0] +=1
                Team_list(pirate,sig)
                return moveTo(count/2,0,pirate)
        else:
            if(count==1):
                s = [X-1,0,(count-1)/2,0]
                Pirate_list(pirate,s)
                sig[0] +=1
                Team_list(pirate,sig)
                return moveTo(X-1,0,pirate)
            else:
                s = [0,(count-1)/2,(count-1)/2,0]
                Pirate_list(pirate,s)
                sig[0] +=1
                Team_list(pirate,sig)
                return moveTo(0,(count-1)/2,pirate)
        
    elif(deploy == (X-1,0)):
        
        if (count%2==0):
            if(count==0):
                s = [X-1,Y-1,count/2,1]
                Pirate_list(pirate,s)
                sig[0] +=1
                Team_list(pirate,sig)
                return moveTo(X-1,Y-1,pirate)
            else:
                s = [X-1-count/2,0,count/2,1]
                Pirate_list(pirate,s)
                sig[0] +=1
                Team_list(pirate,sig)
                return moveTo(X-1-count/2,0,pirate)
        else:
            if(count==1):
                s = [0,0,(count-1)/2,0]
                Pirate_list(pirate,s)
                sig[0] +=1
                Team_list(pirate,sig)
                return moveTo(0,0,pirate)
            else:
                s = [X-1,(count-1)/2,(count-1)/2,0]
                Pirate_list(pirate,s)
                sig[0] +=1
                Team_list(pirate,sig)
                return moveTo(X-1,(count-1)/2,pirate)
        
    else:
        
        if (count%2==0):
            if(count==0):
                s = [X-1,0,count/2,1]
                Pirate_list(pirate,s)
                sig[0] +=1
                Team_list(pirate,sig)
                return moveTo(X-1,0,pirate)
            else:
                s = [X-1-count/2,Y-1,count/2,1]
                Pirate_list(pirate,s)
                sig[0] +=1
                Team_list(pirate,sig)
                return moveTo(X-1-count/2,Y-1,pirate)
        else:
            if(count==1):
                s = [0,Y-1,(count-1)/2,0]
                Pirate_list(pirate,s)
                sig[0] +=1
                Team_list(pirate,sig)
                return moveTo(0,Y-1,pirate)
            else:
                s = [X-1,Y-1-(count-1)/2,(count-1)/2,0]
                Pirate_list(pirate,s)
                sig[0] +=1
                Team_list(pirate,sig)
                return moveTo(X-1,Y-1-(count-1)/2,pirate)
        
    
def ActPirate(pirate):
    
    frame_pirate = pirate.getCurrentFrame() - int(pirate.getID())
    
    X = pirate.getDimensionX()
    Y = pirate.getDimensionY()
    
    deploy = pirate.getDeployPoint()
    pos = pirate.getPosition()
    
    if(pos == deploy and int(pirate.getCurrentFrame())<=121):
        return start(pirate,deploy,X,Y)
    
    
        
    elif(pos!=deploy):
        if(int(pirate.getCurrentFrame())>1500):
            target = Pirate_list(pirate)
            team = Team_list(pirate)
            track = pirate.trackPlayers()
                
            if(len(target)<8):
                if(len(target)<5):
                    target.append(-1)
                    target.append(-1)
                    target.append(-1)
                    Pirate_list(pirate,target)
                elif(len(target)<6):
                    target.append(-1)
                    target.append(-1)
                    Pirate_list(pirate,target)
                elif(len(target)<7):
                    target.append(-1)
                    Pirate_list(pirate,target)
                                   
            if(track[0]=='myCaptured'):
                target[0] = -2
                Pirate_list(pirate,target)
                    
            if(track[1]=='myCaptured'):
                target[1] = -2
                Pirate_list(pirate,target)
                    
            if(track[2]=='myCaptured'):
                target[2] = -2
                Pirate_list(pirate,target)
                    
            if(track[0]!='myCaptured'):
                
                if(target[0]==-1):
                    return random_move(pirate,team[4],team[5],6)
                    
                elif(pos[0]==team[4] and pos[1]==team[5]):
                    target[0] = -1
                    Pirate_list(pirate,target)
                    return random_move(pirate,team[4],team[5],6)
                    
                else:
                    return moveTo(team[4],team[5],pirate)
                    
            elif(track[1]!='myCaptured'):
                    
                if(target[1]==-1):
                    return random_move(pirate,team[6],team[7],6)
                    
                elif(pos[0]==team[6] and pos[1]==team[7]):
                    target[1] = -1
                    Pirate_list(pirate,target)
                    return random_move(pirate,team[6],team[7],6)
                    
                else:
                    return moveTo(team[6],team[7],pirate)
                    
            elif(track[2]!='myCaptured'):
                    
                if(target[2]==-1):
                    return random_move(pirate,team[8],team[9],6)
                    
                elif(pos[0]==team[4] and pos[1]==team[5]):
                    target[0] = -1
                    Pirate_list(pirate,target)
                    return random_move(pirate,team[8],team[9],6)
                    
                else:
                    return moveTo(team[8],team[9],pirate)
        
        elif(len(Pirate_list(pirate))<=4):
            
            target = Pirate_list(pirate)
            current = pirate.investigate_current()
            team = Team_list(pirate)
            
            if((current[0] == "island1" or current[0] == "island2" 
            or current[0] == "island3") and team[int(current[0][-1])]==False):
                
                up = pirate.investigate_up()[0]
                down = pirate.investigate_down()[0]
                left = pirate.investigate_left()[0]
                right = pirate.investigate_right()[0]
                sw = pirate.investigate_sw()[0]
                nw = pirate.investigate_nw()[0]
                se = pirate.investigate_se()[0]
                ne = pirate.investigate_ne()[0]
                
                if(down[0]!= "i" and right[0]== "i" and ne[0]== "i" and left[0]!="i"):
                    team[3+2*(int(current[0][-1])-1)+1] = pos[0]+1
                    team[3+2*(int(current[0][-1])-1)+2] = pos[1]-1
                    team[int(current[0][-1])] = True
                    Team_list(pirate,team)
                    
                elif(down[0]!= "i" and left[0]== "i" and nw[0]== "i" and right[0]!="i"):
                    team[3+2*(int(current[0][-1])-1)+1] = pos[0]-1
                    team[3+2*(int(current[0][-1])-1)+2] = pos[1]-1
                    team[int(current[0][-1])] = True
                    Team_list(pirate,team)
                    
                elif(up[0]!= "i" and left[0]== "i" and se[0]== "i" and right[0]!="i"):
                    team[3+2*(int(current[0][-1])-1)+1] = pos[0]-1
                    team[3+2*(int(current[0][-1])-1)+2] = pos[1]+1
                    team[int(current[0][-1])] = True
                    Team_list(pirate,team)
                    
                elif(up[0]!= "i" and right[0]== "i" and sw[0]== "i" and left[0]!="i"):
                    team[3+2*(int(current[0][-1])-1)+1] = pos[0]+1
                    team[3+2*(int(current[0][-1])-1)+2] = pos[1]+1
                    team[int(current[0][-1])] = True
                    Team_list(pirate,team)
                    
                elif(up[0]== "i" and left[0]!= "i" and down[0]== "i"):
                    team[3+2*(int(current[0][-1])-1)+1] = pos[0]+1
                    team[3+2*(int(current[0][-1])-1)+2] = pos[1]
                    team[int(current[0][-1])] = True
                    Team_list(pirate,team)
                    
                elif(up[0] == "i" and right[0]!= "i" and down[0]== "i"):
                    team[3+2*(int(current[0][-1])-1)+1] = pos[0]-1
                    team[3+2*(int(current[0][-1])-1)+2] = pos[1]
                    team[int(current[0][-1])] = True
                    Team_list(pirate,team)
                    
                elif(right[0]== "i" and left[0]== "i" and up[0]!= "i"):
                    team[3+2*(int(current[0][-1])-1)+1] = pos[0]
                    team[3+2*(int(current[0][-1])-1)+2] = pos[1]+1
                    team[int(current[0][-1])] = True
                    Team_list(pirate,team)
                    
                elif(right[0]== "i" and left[0]== "i" and down[0]!= "i"):
                    team[3+2*(int(current[0][-1])-1)+1] = pos[0]
                    team[3+2*(int(current[0][-1])-1)+2] = pos[1]-1
                    team[int(current[0][-1])] = True
                    Team_list(pirate,team)

            
            if(frame_pirate<=170 and target[3]<4):
                
                if(target[0]==pos[0] and target[1]==pos[1]):
                    
                    if(target[3]%2==0):
                        
                        target[3]+=1
                        
                        if(deploy[0]==0):
                            
                            s = [X-1-target[2],target[1],target[2],target[3]]
                            Pirate_list(pirate,s)
                            return moveTo(s[0],s[1],pirate)
                        
                        elif (deploy[0]==X-1):
                            
                            s = [target[2],target[1],target[2],target[3]]
                            Pirate_list(pirate,s)
                            return moveTo(s[0],s[1],pirate)
                        
                    elif(target[3]%2==1):
                        
                        target[3]+=1
                        
                        if(deploy[1]==0):
                            
                            s = [target[0],Y-1-target[2],target[2],target[3]]
                            Pirate_list(pirate,s)
                            return moveTo(s[0],s[1],pirate)
                        
                        elif(deploy[1]==Y-1):
                            
                            s = [target[0],target[2],target[2],target[3]]
                            Pirate_list(pirate,s)
                            return moveTo(s[0],s[1],pirate)
                            
                else:
                    return moveTo(target[0],target[1],pirate)
                
            elif(frame_pirate<=135):
                n = 1
                if(target[2]%2==0):
                    target[2] = target[2]*2   
                else:
                    target[2] = target[2]*2+1
                    
                if(deploy == (X-1,0)):
                    if(target[2]%2==0):
                        return moveTo(X-1-target[2]-n,0,pirate)
                    else:
                        return moveTo(X-1,target[2]+n,pirate)
                    
                elif(deploy == (0,0)):
                    if(target[2]%2==0):
                        return moveTo(target[2]+n,0,pirate)
                    else:
                        return moveTo(0,target[2]+n,pirate)
                    
                elif(deploy == (0,Y-1)):
                    if(target[2]%2==0):
                        return moveTo(target[2]+n,Y-1,pirate)
                    else:
                        return moveTo(0,Y-1-target[2]-n,pirate)
                    
                elif(deploy == (X-1,Y-1)):
                    if(target[2]%2==0):
                        return moveTo(X-1-target[2]-n,Y-1,pirate)
                    else:
                        return moveTo(X-1,Y-1-target[2]-n,pirate)
                    
            elif(frame_pirate<=195):
                n = 1
                opposite = (X-1-deploy[0],Y-1-deploy[1])
                if(target[2]%2==0):
                    target[2] = target[2]*2   
                else:
                    target[2] = target[2]*2+1
                    
                if(opposite == (X-1,0)):
                    if(target[2]%2==0):
                        return moveTo(X-1-target[2]-n,0,pirate)
                    else:
                        return moveTo(X-1,target[2]+n,pirate)
                    
                elif(opposite == (0,0)):
                    if(target[2]%2==0):
                        return moveTo(target[2]+n,0,pirate)
                    else:
                        return moveTo(0,target[2]+n,pirate)
                    
                elif(opposite == (0,Y-1)):
                    if(target[2]%2==0):
                        return moveTo(target[2]+n,Y-1,pirate)
                    else:
                        return moveTo(0,Y-1-target[2]-n,pirate)
                    
                elif(opposite == (X-1,Y-1)):
                    if(target[2]%2==0):
                        return moveTo(X-1-target[2]-n,Y-1,pirate)
                    else:
                        return moveTo(X-1,Y-1-target[2]-n,pirate)
                    
            elif(frame_pirate<=1500):
                
                track = pirate.trackPlayers()
                count = 2*team[-1]/3
                flag2 = 0
                
                for x in (-3,0):
                    if(track[x]=='oppCapturing'):
                        flag2 = -2-x
                        break
                        
                if((team[-2]+team[-3]+team[-4])<=2):
                    if(team[1]==True and track[0]!='myCaptured' and track[3] == '' and team[10]<max(17,count/2)):
                        team[-4] = 1
                        Team_list(pirate,team)
                        return island(pirate,1)
                    
                    elif(team[2]==True and track[1]!='myCaptured' and track[4] == '' and team[11]<max(17,count/2)):
                        team[-3] = 1
                        Team_list(pirate,team)
                        return island(pirate,2)
                    
                    elif(team[3]==True and track[2]!='myCaptured' and track[5] == '' and team[12]<max(17,count/2)):
                        team[-2] = 1
                        Team_list(pirate,team)
                        return island(pirate,3)
                    
                    else:
                        if(track[-3]=='oppCaptured'):
                            return moveTo(team[4],team[5],pirate)
                        elif(track[-2]=='oppCaptured'):
                            return moveTo(team[6],team[7],pirate)
                        elif(track[-1]=='oppCaptured'):
                            return moveTo(team[8],team[9],pirate)
                        else:
                            return gandmasti(pirate,X/2,Y/2)
                
                elif(flag2!=0):
                    if(team[flag2]==True):                       
                        return gandmasti(pirate,team[3+2*(flag2-1)+1],team[3+2*(flag2-1)+2])
                    
                    else:
                        return gandmasti(pirate,X/2,Y/2)
                    
                else:
                    if(track[-3]=='oppCaptured'):
                        return moveTo(team[4],team[5],pirate)
                    elif(track[-2]=='oppCaptured'):
                        return moveTo(team[6],team[7],pirate)
                    elif(track[-1]=='oppCaptured'):
                        return moveTo(team[8],team[9],pirate)
                    else:
                        return gandmasti(pirate,X/2,Y/2)
                                                                        
        else:
            team = Team_list(pirate)
            target = Pirate_list(pirate)
            track = pirate.trackPlayers()
        
            up = pirate.investigate_up()
            down = pirate.investigate_down()
            left = pirate.investigate_left()
            right = pirate.investigate_right()
            sw = pirate.investigate_sw()
            nw = pirate.investigate_nw()
            se = pirate.investigate_se()
            ne = pirate.investigate_ne()
            
            if(target[5]>0 and -17<target[4]<0):
                if track[target[5]-1]=='myCaptured':
                    team[-5+target[5]] = 0
                    target.pop()
                    target.pop()
                    Team_list(pirate,team)
                    Pirate_list(pirate,target)
                    return 0
                
                elif(track[1-target[5]]=='oppCapturing' or track[target[5]-1]==''):
                    target[4]=0
                    team[target[5]+9]-=1
                    Team_list(pirate,team)
                    Pirate_list(pirate,target)
                    return moveTo(team[3+2*(target[5]-1)+1],team[3+2*(target[5]-1)+2],pirate)
                
            
            if(0<target[5]<4):
                if(up[0][0]=="i" or down[0][0]=="i" or left[0][0]=="i" or right[0][0]=="i" 
                or sw[0][0]=="i" or nw[0][0]=="i" or se[0][0]=="i" or ne[0][0]=="i"):
                    if(up[1][0]=="e" or down[1][0]=="e" or left[1][0]=="e" or right[1][0]=="e" 
                or sw[1][0]=="e" or nw[1][0]=="e" or se[1][0]=="e" or ne[1][0]=="e"):
                        team[target[5]+12] = True
                        Team_list(pirate,team)             
            
            if(target[0] == pos[0] and target[1] == pos[1] and target[4] == 0):
                n = target[5]
                target[5] = -1
                target[4] = -n - 16
                Pirate_list(pirate,target)
                return random_move(pirate,team[3+2*(n-1)+1],team[3+2*(n-1)+2],5)
            
            elif(target[4]==-17 or target[4]==-18 or target[4]==-19):
                n = -target[4]-16
                return random_move(pirate,team[3+2*(n-1)+1],team[3+2*(n-1)+2],5)
            
            elif(target[0] == pos[0] and target[1] == pos[1] and target[4]>0):
                target[4] = -target[4]
                Pirate_list(pirate,target)
                return circle(pirate)
            
            elif(target[4]<0):
                return circle(pirate)
            
            else:
                return moveTo(target[0],target[1],pirate)
            
def ActTeam(team):
    
    if team.getTeamSignal() == "" :
        total = int(team.getTotalPirates())
        s = [0,False,False,False,0,0,0,0,0,0,0,0,0,False,False,False,0,0,0,total]
        team.setTeamSignal(f"{s}")
        
    else:
        s = ast.literal_eval(team.getTeamSignal())
        s[-1] = int(team.getTotalPirates())
        team.setTeamSignal(f"{s}")
    
    s = ast.literal_eval(team.getTeamSignal())
    for n in (1,4):
        if(s[n+12]==True):
            team.buildWalls(n)   
            
    if(int(team.getCurrentFrame())>1600):
        team.buildWalls(1)
        team.buildWalls(2)
        team.buildWalls(3)
     