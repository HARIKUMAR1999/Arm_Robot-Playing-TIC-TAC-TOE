% Open a serial connection with the Picasso robot
% Close previous serial connections
previous=instrfind('Type','serial');
if(~isempty(previous))
    fclose(previous);
end

port=serialport('COM7','BaudRate',9600,'DataBits',8,'Parity','none',...
'StopBits',1,'Timeout',5000,'Terminator',13);
pause(0.5);
if(~isempty(port)) 
    fopen(port); pause(0.5);
end

% Turn Servos on
command=sprintf('PRN SVO'); fprintf(port, command); pause(3);

command=sprintf('PRN MP,%1.1f,%1.1f,%1.1f',350.93,-104.65,288.92);fprintf(port,command); pause(.3);
while true

    data = textscan('C:\Users\nitin\Downloads\Second Method Tic Tac Toe\A.txt');
    b=data;

    if b==1
        % % Draw Circle Location 1
        command=sprintf('PRN MP,%1.1f,%1.1f,%1.1f',230,10,250);fprintf(port,command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',4,230, 10, 231);fprintf(port, command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',5,240, 20, 231);fprintf(port, command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',6,230, 30, 231);fprintf(port, command); pause(.3);
        command =sprintf('PRN MDPC,%1.1f,%1.1f,%1.1f',4,5,6); fprintf(port, command); pause(.3);
        pause(1);
        command=sprintf('PRN MP,%1.1f,%1.1f,%1.1f',350.93,-104.65,288.92);fprintf(port,command); pause(.3);
        pause(5);
        file2 = fopen("C:\Users\nitin\Downloads\Second Method Tic Tac Toe\A.txt","w");
        fprintf(file2,'%d',30);
        fclose(file2);
    end
    
    if b==2
        % % % Draw Circle Location 2
        command=sprintf('PRN MP,%1.1f,%1.1f,%1.1f',245,75,250);fprintf(port,command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',4,245, 75, 231);fprintf(port, command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',5,255, 85, 231);fprintf(port, command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',6,245, 95, 231);fprintf(port, command); pause(.3);
        command =sprintf('PRN MDPC,%1.1f,%1.1f,%1.1f',4,5,6); fprintf(port, command); pause(.3);
        pause(1);
        command=sprintf('PRN MP,%1.1f,%1.1f,%1.1f',350.93,-104.65,288.92);fprintf(port,command); pause(.3);
        pause(5);
        file2 = fopen("C:\Users\nitin\Downloads\Second Method Tic Tac Toe\A.txt","w");
        fprintf(file2,'%d',30);
        fclose(file2);
    end
    
    if b==3
        % % Draw Circle Location 3
        command=sprintf('PRN MP,%1.1f,%1.1f,%1.1f',255,140,250);fprintf(port,command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',4,255, 140, 231);fprintf(port, command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',5,265, 150, 231);fprintf(port, command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',6,255, 160, 231);fprintf(port, command); pause(.3);
        command =sprintf('PRN MDPC,%1.1f,%1.1f,%1.1f',4,5,6); fprintf(port, command); pause(.3);
        pause(1);
        command=sprintf('PRN MP,%1.1f,%1.1f,%1.1f',350.93,-104.65,288.92);fprintf(port,command); pause(.3);
        pause(5);
        file2 = fopen("C:\Users\nitin\Downloads\Second Method Tic Tac Toe\A.txt","w");
        fprintf(file2,'%d',30);
        fclose(file2);
    end
    
    if b==4
        % % Draw Circle Location 4
        command=sprintf('PRN MP,%1.1f,%1.1f,%1.1f',275,-20,250);fprintf(port,command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',4,275, -15, 231);fprintf(port, command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',5,285, -5, 231);fprintf(port, command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',6,275, 5, 231);fprintf(port, command); pause(.3);
        command =sprintf('PRN MDPC,%1.1f,%1.1f,%1.1f',4,5,6); fprintf(port, command); pause(.3);
        pause(1);
        command=sprintf('PRN MP,%1.1f,%1.1f,%1.1f',350.93,-104.65,288.92);fprintf(port,command); pause(.3);
        pause(5);
        file2 = fopen("C:\Users\nitin\Downloads\Second Method Tic Tac Toe\A.txt","w");
        fprintf(file2,'%d',30);
        fclose(file2);
    end
    
    if b==5
        % % % Draw Circle Location 5
        command=sprintf('PRN MP,%1.1f,%1.1f,%1.1f',295,55,250);fprintf(port,command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',4,295,55,231);fprintf(port, command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',5,305, 65, 231);fprintf(port, command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',6,295, 75, 231);fprintf(port, command); pause(.3);
        command =sprintf('PRN MDPC,%1.1f,%1.1f,%1.1f',4,5,6); fprintf(port, command); pause(.3);
        pause(1);
        command=sprintf('PRN MP,%1.1f,%1.1f,%1.1f',350.93,-104.65,288.92);fprintf(port,command); pause(.3);
        pause(5);
        file2 = fopen("C:\Users\nitin\Downloads\Second Method Tic Tac Toe\A.txt","w");
        fprintf(file2,'%d',30);
        fclose(file2);
    end
    
    if b==6
        % % % Draw Circle Location 6
        command=sprintf('PRN MP,%1.1f,%1.1f,%1.1f',315,105,250);fprintf(port,command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',4,315,105,231);fprintf(port, command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',5,325, 115, 231);fprintf(port, command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',6,315, 125, 231);fprintf(port, command); pause(.3);
        command =sprintf('PRN MDPC,%1.1f,%1.1f,%1.1f',4,5,6); fprintf(port, command); pause(.3);
        pause(1);
        command=sprintf('PRN MP,%1.1f,%1.1f,%1.1f',350.93,-104.65,288.92);fprintf(port,command); pause(.3);
        pause(5);
        file2 = fopen("C:\Users\nitin\Downloads\Second Method Tic Tac Toe\A.txt","w");
        fprintf(file2,'%d',30);
        fclose(file2);
    end
    
    
    if b==7
        % % Draw Circle Location 7
        command=sprintf('PRN MP,%1.1f,%1.1f,%1.1f',330,-40,250);fprintf(port,command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',4,330, -40, 231);fprintf(port, command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',5,340, -30, 231);fprintf(port, command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',6,330, -20, 231);fprintf(port, command); pause(.3);
        command =sprintf('PRN MDPC,%1.1f,%1.1f,%1.1f',4,5,6); fprintf(port, command); pause(.3);
        pause(1);
        command=sprintf('PRN MP,%1.1f,%1.1f,%1.1f',350.93,-104.65,288.92);fprintf(port,command); pause(.3);
        pause(5);
        file2 = fopen("C:\Users\nitin\Downloads\Second Method Tic Tac Toe\A.txt","w");
        fprintf(file2,'%d',30);
        fclose(file2);
    end
    
    if b==8
        % % Draw Circle Location 8
        command=sprintf('PRN MP,%1.1f,%1.1f,%1.1f',360,30,250);fprintf(port,command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',4,360, 30, 231);fprintf(port, command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',5,370, 40, 231);fprintf(port, command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',6,360, 50, 231);fprintf(port, command); pause(.3);
        command =sprintf('PRN MDPC,%1.1f,%1.1f,%1.1f',4,5,6); fprintf(port, command); pause(.3);
        pause(1);
        command=sprintf('PRN MP,%1.1f,%1.1f,%1.1f',350.93,-104.65,288.92);fprintf(port,command); pause(.3);
        pause(5);
        file2 = fopen("C:\Users\nitin\Downloads\Second Method Tic Tac Toe\A.txt","w");
        fprintf(file2,'%d',30);
        fclose(file2);
    end
    
    if b==9
        % % Draw Circle Location 9
        command=sprintf('PRN MP,%1.1f,%1.1f,%1.1f',375,90,250);fprintf(port,command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',4,375, 90, 231);fprintf(port, command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',5,385, 100, 231);fprintf(port, command); pause(.3);
        command=sprintf('PRN PD,%1.1f,%1.1f,%1.1f,%1.1f',6,375, 110, 231);fprintf(port, command); pause(.3);
        command =sprintf('PRN MDPC,%1.1f,%1.1f,%1.1f',4,5,6); fprintf(port, command); pause(.3);
        pause(1);
        command=sprintf('PRN MP,%1.1f,%1.1f,%1.1f',350.93,-104.65,288.92);fprintf(port,command); pause(.3);
        pause(5);
        file2 = fopen("C:\Users\nitin\Downloads\Second Method Tic Tac Toe\A.txt","w");
        fprintf(file2,'%d',30);
        fclose(file2);
    end
    pause(2);
end
