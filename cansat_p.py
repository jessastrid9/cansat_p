from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from decimal import Decimal
import math
import random
import sys
import binascii
import csv
import serial
import numpy as np
from qwt import (QwtPlot, QwtPlotMarker, QwtLegend, QwtPlotGrid, QwtPlotCurve,
                 QwtPlotItem, QwtText, QwtLegendData, QwtLinearColorMap,
                 QwtInterval, QwtScaleMap, toQImage)
global lat1
global long1
global flag1


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        principal_widget = Principal(self)
        principal_widget.b3.clicked.connect(self.StartMission)
        flag1=0
        self.central_widget.addWidget(principal_widget)
        self.resize(1900, 900)
        self.setWindowTitle('TEAM THOR CANSAT COMPETITION')
        self.setWindowIcon(QIcon("equipothoricon.png"))
        print("hola")
    def StartMission(self):
        mision_widget = Mision(self)
        self.central_widget.addWidget(mision_widget)
        self.central_widget.setCurrentWidget(mision_widget)
        flag1=1
        print("empezarM")


class Principal(QWidget):
    def __init__(self, parent=None):
        super(Principal, self).__init__(parent)
        layout1 =QHBoxLayout()
###################################
        self.resize(1900, 900)
        self.setWindowTitle('CANSAT')
        ##FUNCIONES
        def Configbutton(button, y, ev1): #Configuracion de botones
            button.setStyleSheet('QPushButton {background-color: rgb(220, 220, 220); color: black; border-radius: 10px; border-style: outset;border-width: 6px;border-color: rgb(100,18,18)}')
            # font= QFont("Calibri", 20, 89, 0);  #### FUENTE, TAMAÑO, GROSOR, ITALICA 0-F
            button.setFont(QFont("UKNumberPlate", 20, 89, 0))
            button.setGeometry(450, y, 400, 100)  # Posicion

            if ev1!=0: #no entra con el b3
                button.clicked.connect(ev1)  # event
####################################
        def Scan():

            layout1.lb3.setPixmap(QPixmap("ipn.png"))
            layout1.lb3.setGeometry(900, 4, 100, 200)
            # FLIGHT_<4784>.csv
            # [GPS, BSY][IMU, BSY][DPS, BSY]
            #layout.GPSText.setText("GPS... Ready!")
            #layout.GPSText.setFont(font)
            #layout.GPSText.setGeometry(900, 25, 200, 100)

            #layout.IMUText.setText("IMU... Ready!")
            #layout.IMUText.setFont(font)
            #layout.IMUText.setGeometry(900, 25, 200, 100)

            #layout.GPSText.setText("GPS... Ready!")
            #layout.GPSText.setFont(font)
            #layout.GPSText.setGeometry(900, 25, 200, 100)


        def AltitudeCal():
            print("Altitude")  #####empieza mision
            layout1.lb4.setPixmap(QPixmap("ipn.png"))
            layout1.lb4.setGeometry(900, 200, 100, 200)
        # IMAGENES
        layout1.lb1 = QLabel(self)
        layout1.lb3 = QLabel(self)
        layout1.lb4 = QLabel(self)
        layout1.lb5 = QLabel(self)
        layout1.lb6 = QLabel(self)
        layout1.lb7 = QLabel(self)
        layout1.lb8 = QLabel(self)
        layout1.lb1.setPixmap(QPixmap("CANSAT_BKG.png"))
        layout1.lb1.setGeometry(0, 0, 1500, 1000)
        layout1.lb4.setPixmap(QPixmap("ipn.png"))
        layout1.lb4.setGeometry(1250, 0, 120, 90)
        layout1.lb3.setPixmap(QPixmap("mexico.png"))
        layout1.lb3.setGeometry(1160, 0, 120, 90)
        layout1.lb5.setPixmap(QPixmap("upiita.png"))
        layout1.lb5.setGeometry(80, 0, 120, 90)
        layout1.lb6.setPixmap(QPixmap("TEAM2.png"))
        layout1.lb6.setGeometry(500, 25, 300, 80)
        layout1.lb7.setPixmap(QPixmap("CANSATCOMP.png"))
        layout1.lb7.setGeometry(480, 60, 180, 90)
        layout1.lb8.setPixmap(QPixmap("IPNUPIITA.png"))
        layout1.lb8.setGeometry(680, 60, 180, 90)

        # BOTONES
        b1 = QPushButton('Scan', self)
        b2 = QPushButton('Altitude Calibration', self)
        self.b3 = QPushButton('Start Mission', self)
        Configbutton(b1, 150, Scan)  # config boton1
        Configbutton(b2, 310, AltitudeCal)
        Configbutton(self.b3, 490, 0)
        layout1.TeamT = QLabel(self)

        self.setLayout(layout1)

class Mision(QWidget):
    def __init__(self, parent=None):
        super(Mision, self).__init__(parent)
        layout = QGridLayout(self)
        layout.lb1 = QLabel(self)
        layout.IM1=QLabel(self)
        layout.IM2=QLabel(self)
        layout.IM3=QLabel(self)
        layout.IM4 = QLabel(self)
        layout.IM5 = QLabel(self)
        layout.IM1.setPixmap(QPixmap("ipn.png"))
        layout.IM1.setGeometry(1250, 0, 120, 90)
        layout.IM2.setPixmap(QPixmap("mexico.png"))
        layout.IM2.setGeometry(1160, 0, 120, 90)
        layout.IM3.setPixmap(QPixmap("upiita.png"))
        layout.IM3.setGeometry(80, 0, 120, 90)
        layout.IM4.setPixmap(QPixmap("CANSATCOMP.png"))
        layout.IM4.setGeometry(500, 30, 180, 90)
        layout.IM5.setPixmap(QPixmap("IPNUPIITA.png"))
        layout.IM5.setGeometry(700, 30, 180, 90)

        ###############
        layout.lb1.setPixmap(QPixmap("CANSAT_BKG.png"))
        layout.lb1.setGeometry(0, 0, 1500, 1000)

        ############################TITLE#############################
        titulo1=QLabel()
        teamthor = QPixmap("TEAM3.png")
        titulo1.setPixmap(teamthor)
        layout.addWidget(titulo1,0,1)
        #############################################################
        layout.addWidget(grap1, 1, 0)
 ##############################################################
        layoutpos = QGridLayout()
        layoutposH = QHBoxLayout()
        layoutposV = QVBoxLayout()
        layoutpos.addWidget(graph2, 0, 0)
        labeln = QLabel()
        pixmappos = QPixmap("cansatImg.png")
        pixmappos = pixmappos.scaledToWidth(50)
        labeln.setPixmap(pixmappos)
        layoutposH.addWidget(text_space2)
        layoutposH.addWidget(labeln)
        layoutposV.addWidget(text_space3)
        layoutposV.addLayout(layoutposH)
        layoutposV.addWidget(text_space4)
        # layoutposV.addLayout(layoutposH)
        layoutpos.addLayout(layoutposV, 0, 0)
        layout.addLayout(layoutpos, 2, 0)
        layout.IM6 = QLabel(self)
        layout.IM6.setPixmap(QPixmap("ground.png"))
        layout.IM6.setGeometry(250, 472, 120, 90)
#############################################################)
        layoutv = QGridLayout()
        layoutvN = QVBoxLayout()
        lb1 = QLabel(self)
        pixmap=QPixmap("DIAL4.png")
        pixmap = pixmap.scaledToWidth(220)
        lb1.setPixmap(pixmap)
        layoutv.addWidget(text_pressure,0,0)
        layoutv.addWidget(lb1,1,0)
        layoutv.addWidget(ql1,1,0,Qt.AlignCenter)
        frame5.setLayout(layoutv)
        layoutvN.addWidget(frame5)
        layout.addLayout(layoutvN, 1, 1)
#############################################################
        layoutvp = QGridLayout()
        layoutvNp = QVBoxLayout()
        lb1p = QLabel(self)
        pixmapp = QPixmap("DIAL4.png")
        pixmapp = pixmap.scaledToWidth(160)
        lb1p.setPixmap(pixmapp)
        layoutvp.addWidget(text_pitch, 0, 0)
        layoutvp.addWidget(text_roll, 1, 0)
        layoutvp.addWidget(text_bladespin, 2, 0)
        layoutvp.addWidget(lb1p, 3, 0 ,Qt.AlignCenter)
        layoutvp.addWidget(ql1p, 3, 0, Qt.AlignCenter)
        frame6.setLayout(layoutvp)
        layoutvNp.addWidget(frame6)
        layout.addLayout(layoutvNp, 2, 1)
############################################################
        layouth1 = QHBoxLayout()
        layouth2 = QHBoxLayout()
        layouth1.addWidget(volt_bar)
        layouth1.addWidget(text_volt)
        frame3.setLayout(layouth1)
        layouth2.addWidget(frame3)
        layout.addLayout(layouth2, 1, 2)
############################################################
        layoutG = QVBoxLayout()
        layoutG2 = QVBoxLayout()
        layoutG3 = QVBoxLayout()
        layoutG4 = QVBoxLayout()
        layoutG5 = QVBoxLayout()
        layoutG.addWidget(text_gps_time)
        layoutG.addWidget(text_gps_la)
        layoutG.addWidget(text_gps_lo)
        layoutG.addWidget(text_gps_al)
        layoutG.addWidget(text_gps_sats)
        layoutG3.addWidget(text_teamId)
        layoutG3.addWidget(text_mission_time)
        layoutG3.addWidget(text_Packet_count)
        frame2.setLayout(layoutG)
        frame7.setLayout(layoutG3)
        layoutG2.addWidget(frame2)
        layoutG4.addWidget(frame7)
        layoutG5.addLayout(layoutG2)
        layoutG5.addLayout(layoutG4)
        layout.addLayout(layoutG5, 2,2)
############################################################
        vboxj3 = QVBoxLayout()
        layoutG3 = QVBoxLayout()
        vboxj3.addWidget(text_sys)
        vboxj3.addWidget(text_elevation)
        vboxj3.addWidget(text_azimut)
        vboxj3.addWidget(text_gs_to_cansat)
        vboxj3.addWidget(text_space)
        frame1.setLayout(vboxj3)
        layoutG3.addWidget(frame1)
        layout.addLayout(layoutG3, 1, 3)
###########################################################
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(30)
############################################################
        layouth3 = QHBoxLayout()
        layouth4 = QHBoxLayout()
        layouth3.addWidget(temp_bar)
        layouth3.addWidget(temp_text)
        frame4.setLayout(layouth3)
        layouth4.addWidget(frame4)
        layout.addLayout(layouth4, 2, 3)
        temp_bar.setStyleSheet('QProgressBar::chunk {background: rgb(255, 0, 0);}')
        temp_bar.setRange(0, 350)
        temp_bar.setFixedSize(50, 200)
############################################################
        self.setLayout(layout)

############################# PLOT CLASS
class DataPlot(QwtPlot):
    def __init__(self, *args):
        QwtPlot.__init__(self, *args)

        self.setCanvasBackground(Qt.white)
        curva = QwtPlotCurve('Altitud')
        self.phase=0
        ##################################################
        # Initialize data
        self.x = [0]
        self.y = [0]
        # Title of the graph
        self.g1title = "Altitude= " + str(self.x[0])
        self.insertLegend(QwtLegend(), QwtPlot.BottomLegend);
        self.curveR = QwtPlotCurve("Altitude")
        self.curveR.attach(self)
        self.curveR.setPen(QPen(Qt.blue))
        self.setAxisTitle(QwtPlot.xBottom, "Time (seconds)")
        self.setAxisTitle(QwtPlot.yLeft, "Altitude(m)")
        self.setAxisScale(QwtPlot.xBottom, 0.0, 500)
        self.setAxisScale(QwtPlot.yLeft, 0.0, 1200)
        self.pal = QPalette()  #####palette for background
        self.pal.setColor(QPalette.Text, Qt.white)
        self.pal.setColor(QPalette.Foreground, Qt.white)
        self.setPalette(self.pal)
        self.counter=0 ###counter for actualize data, is the same for all of the graphs/data
        grid = QwtPlotGrid()
        grid.attach(self)
        grid.setPen(QPen(Qt.black, 0, Qt.DotLine))
######################################### TEXT CLASS ################################
class Textc(QLabel):
    def __init__(self, *args):
        QLabel.__init__(self, *args)
        self.font1 = QFont("Adobe Gothic Std B", 11, 8, 0);  #### FUENTE, TAMAÑO, GROSOR, ITALICA 0-F
        self.setFont(self.font1)
        self.setStyleSheet('color: white')
######################################### PROGRESS BAR CLASS ####################
class Pbar(QProgressBar):
    def __init__(self, *args):
        QProgressBar.__init__(self, *args)
        self.setGeometry(1190, 465, 40, 240)
        self.setOrientation(Qt.Vertical)
        self.setRange(0,12)
        self.setFixedSize(50,250)
        self.move(50,200)
        #self.setStyleSheet('QProgressBar::chunk {background: rgb(255, 0, 0);}')
########################### FRAME CLASS #############################
class Marco(QFrame):
    def __init__(self, *args):
        QFrame.__init__(self, *args)
        self.setFrameShape( QFrame.Box| QFrame.Raised )
        self.setLineWidth(3)
        self.setMidLineWidth(1)
##########################################################
class needle(QLabel):
    def __init__(self, *args):
        QLabel.__init__(self, *args)
#########################################################
class data:
    def __init__(self, press,mtime,packetc,alt,temp,volt,gpst,gpsla,gpslo,gpsalt,gpssats,pitch,roll,blade):
        self.press=press
        self.mtime=mtime
        self.packetc=packetc
        self.alt=alt
        self.temp=temp
        self.volt=volt
        self.gpst=gpst
        self.gpsla=gpsla
        self.gpslo = gpslo
        self.gpsalt=gpsalt
        self.gpssats=gpssats
        self.pitch=pitch
        self.roll=roll
        self.blade=blade


if __name__ == '__main__':
    app =QApplication([])
    ser = serial.Serial('COM35', baudrate=115200, timeout=.085)
    #self.ser = serial.Serial('COM35', baudrate=115200, timeout=.085)
    window = MainWindow()
    ################OBJECTS#####################
    grap1=DataPlot()
    graph2 = DataPlot()
    graph2.setAxisTitle(QwtPlot.xBottom, "x(m)")
    graph2.setAxisTitle(QwtPlot.yLeft, "y(m)")
    graph2.setAxisScale(QwtPlot.xBottom, -800, 800)
    graph2.setAxisScale(QwtPlot.yLeft, -800, 800)
    text_pressure=Textc()
    text_volt = Textc()
    text_gps_time= Textc()
    text_gps_la = Textc()
    text_gps_lo= Textc()
    text_gps_al = Textc()
    text_gps_sats = Textc()
    text_teamId = Textc()
    text_teamId.setText("Team Id= 2280")
    text_mission_time = Textc()
    text_Packet_count = Textc()
    text_sys=Textc()
    text_sys.setText("System Tracking")
    text_elevation = Textc()
    text_azimut = Textc()
    text_gs_to_cansat = Textc()
    temp_text=Textc()
    text_pitch = Textc()
    text_roll = Textc()
    text_bladespin = Textc()
    text_space= Textc()
    text_alt = Textc()
    text_space2 = Textc()
    text_space3 = Textc()
    text_space.setText(' ' * 75)  ## SET SPACE TO LAST FRAME
    text_space4 = Textc()
    volt_bar= Pbar()
    temp_bar=Pbar()
    frame1=Marco()
    frame2 = Marco()
    frame3 = Marco()
    frame4 =Marco()
    frame5= Marco()
    frame6 = Marco()
    frame7 = Marco()
    pixmap2 = QPixmap("pointer1.png")
    pixmap2 = pixmap2.scaledToWidth(100)
    pixmap2p = QPixmap("pointer1.png")
    pixmap2p = pixmap2.scaledToWidth(80)
    ql1=QLabel()
    ql1p=QLabel()
    xRef0 = 95
    yRef0 = 370
    xRef1 = 95
    yRef1 = 370
    error = 0
    teamId = '';
    missionTime = '';
    packetCount = '';
    altitude = '';
    pressure = '';
    temp = '';
    voltage = '';
    gpsTime = '';
    gpsLatitude = '';
    gpsLongitude = '';
    gpsAltitude = '';
    gpsSats = '';
    pitch = '';
    roll = '';
    bladeSpin = '';
    softwareState = '';
    bonusDirection = '';
    valorAnterior = 0;
    alturaRect = 0;
    auxTiempo = 0;
    auxAltura = 0;
    xTiempo0 = 0;
    xTiempo1 = 0;
    auxPosX0 = 0;
    auxPosY0 = 0;
    barometro = 0;
    velocimetro = 0;
    pila = 0;
    press = ''
    blade = ''
    xPos = 0;
    yPos = 0;
    elevacion = 0;
    azimutCalib = 0;
    distancia = 0;
    temperatura = 0;
    temp2 = 0;
    data=data(0,0,0,0,0,0,0,0,0,0,0,0,0,0)

#############################################
    def calculaDistancia(lat1, long1, gpsLatitude, gpsLongitude):
        #
        if lat1 == gpsLatitude or long1 == gpsLongitude:
            return 0;
        else:
            # Origen
            lat1 = 32.211530
            long1 = -98.234009
            radlat1 = (math.pi * float(lat1)) / 180;
            radlat2 = (math.pi * float(gpsLatitude)) / 180;
            radlon1 = (math.pi * float(long1)) / 180;
            theta = float(long1) - float(gpsLongitude);
            phi = float(lat1) - float(gpsLatitude);
            radphi = (math.pi * phi) / 180;
            radtheta = (math.pi * theta) / 180;
            dist = (math.sin(radlat1) * math.sin(radlat2)) + (
                        math.cos(radlat1) * math.cos(radlat2) * math.cos(radtheta))
            if dist > 1:
                dist = 1
            dist = math.acos(dist)
            dist = dist * 180 / math.pi
            dist = dist * 60 * 1.1515 * 1.609344 * 1000;
            dist2 = float("{0:.2f}".format(dist))
            return dist2

    def calculaEleva(distancia, altitude):
        anguloEleva = math.atan(float(altitude) / distancia);
        anguloElevaGrados = (anguloEleva * 180 / math.pi);
        anguloElevaGradosDos = float("{0:.2f}".format(anguloElevaGrados))
        return anguloElevaGradosDos


    def calculaAzimut(lat1, long1, gpsLatitude, gpsLongitude):
        # gpsLatitude = 32.221959
        # gpsLongitude = -98.216269
        # Origen
        lat1 = 32.211530
        long1 = -98.234009
        radlat1 = (math.pi * float(lat1)) / 180;
        radlat2 = (math.pi * float(gpsLatitude)) / 180;
        radlon1 = (math.pi * float(long1)) / 180;
        theta = float(long1) - float(gpsLongitude);
        radtheta = (math.pi * theta) / 180;
        b = math.sin(radtheta) * math.cos(radlat2);
        a = (math.cos(radlat1) * math.sin(radlat2)) - (math.sin(radlat1) * math.cos(radlat2) * math.cos(radtheta));
        anguloAzimut = math.atan2(b, a);
        anguloAzimutGrados = -(anguloAzimut * 180) / math.pi;
        anguloAzimutGradosDos = float("{0:.2f}".format(anguloAzimutGrados))
        return anguloAzimutGradosDos;


    def calculaX(azimut, distancia):
        azimutRad = (math.pi * azimut) / 180;
        X = distancia * math.sin(azimutRad)
        X2 = float("{0:.2f}".format(X))
        return X2;


    def calculaY(azimut, distancia):
        azimutRad = (math.pi * azimut) / 180;
        Y = distancia * math.cos(azimutRad)
        Y2 = float("{0:.2f}".format(Y))
        return Y2;


    def calculaAzimutCalib(anguloAzimutGrados):
        if (anguloAzimutGrados < 0):
            anguloAzimutGradosCalib = anguloAzimutGrados + 360 + 40;
        else:
            anguloAzimutGradosCalib = anguloAzimutGrados + 40;
        return anguloAzimutGradosCalib;


    ###################SERIAL CONNECTION################################################
    def serial_connection():
        ser.flushInput()
        #print("serial")
        sys.stdout.flush()
        ser.flushInput()
        ser.flushOutput()
        palabra = 0
        ser.read(ser.inWaiting())
        palabra = ser.readline()
        palabra = palabra.decode('utf-8')
        #print(str(palabra))
        x = palabra.rfind('<')
        y = palabra.rfind('>')
        z = palabra.rfind('><')
        if x == -1 or y == -1 or z != -1:  # Busca los corchetes.... si no los encuentra, paquete incompleto y z!=-1 quiere decir que si está el "><"
            print('Paquete incompleto, Error')
        else:
            palabraSep = palabra.split("<")
            l = 0;
            palabraSep.pop(0)  ##quitamos el vacío
            while l < len(palabraSep):
                palabraSeparada = palabraSep[l].split(",")  # divide los campos
                for camposTotal in palabraSeparada:
                    if camposTotal == '': #inicio del paquete
                        palabraSeparada.pop(0)  # quitamos la bandera del paquete
                        i = 0;
                        while i < len(palabraSeparada):
                            if palabraSeparada[i] == '>':  # fin de paquete, paquete exitoso!
                                print("Se detecta fin de paquete, es decir el paquete: " + packetCount + " es Exitoso");
                                if valorAnterior == packetCount:
                                    print("Se repite paquete, no guardes: " + packetCount);
                                    valorA = 0
                                else:
                                    #valorAnterior = packetCount
                                    with open('flight_4784.csv', mode='a', newline='') as fp:
                                        #print("with")
                                        a = csv.writer(fp, delimiter=',')
                                        fila = [];
                                        fila.append(teamId)
                                        fila.append(missionTime)
                                        fila.append(packetCount)
                                        fila.append(altitude)
                                        fila.append(pressure)
                                        fila.append(temp)
                                        fila.append(voltage)
                                        fila.append(gpsTime)
                                        fila.append(gpsLatitude)
                                        fila.append(gpsLongitude)
                                        fila.append(gpsAltitude)
                                        fila.append(gpsSats)
                                        fila.append(pitch)
                                        fila.append(roll)
                                        fila.append(bladeSpin)
                                        fila.append(softwareState)
                                        fila.append(bonusDirection)
                                        a.writerow(fila)
                                print(pressure)

                                packetCountAck = '<'
                                packetCountAck += packetCount
                                packetCountAck += '>'
                                ser.write(packetCountAck.encode())
                                l += 1
                                break
                            subPalab = palabraSeparada[i].split('*')
                            #print(subPalab[1])
                            checkSumSource2Ascii = binascii.unhexlify(subPalab[1]).decode('utf-8')
                            subPalabList = list(subPalab[0])
                            # print(len(subPalabList))
                            # print(subPalabList)
                            coma = ","
                            j = 0
                            while j < len(subPalabList):
                                # print(subPalabList[j]);
                                if j == 0:
                                    sumaXor = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(coma, subPalabList[j]));
                                else:
                                    sumaXor = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(sumaXor, subPalabList[j]));
                                j += 1;
                            if sumaXor == checkSumSource2Ascii:
                                sumaXor;
                                # print("Campo Exitoso");
                            else:
                                print("Campo Erróneo, Paquete erróneo, espera reenvío")
                                error += 1;
                                # No hacer nada y esperar nuevo paquete
                                # l = 0;
                                l = len(palabraSep);  # libera loop
                                break;

                            if (i == 0):
                                # print("TeamID: " + subPalab[0])
                                teamId = subPalab[0];

                            if (i == 1):
                                # print("Mission Time: " + subPalab[0])
                                missionTime = subPalab[0];
                                data.mtime=missionTime
                            if (i == 2):
                                # print("Packet Count: " + subPalab[0])
                                packetCount = subPalab[0];
                                data.packetc=packetCount
                                # print() #imprime el payload de campo 3
                            if (i == 3):
                                # print("Altitude: " + subPalab[0])
                                altitude = subPalab[0];
                                data.alt=altitude
                            if (i == 4):
                                # print("Pressure: " + subPalab[0])
                                pressure = subPalab[0];
                                data.press=pressure
                            if (i == 5):
                                # print("Temp: " + subPalab[0])
                                temp = subPalab[0];
                                data.temp=temp
                            if (i == 6):
                                # print("Voltage: " + subPalab[0])
                                voltage = subPalab[0];
                                data.volt=voltage
                            if (i == 7):
                                # print("GPS time: " + subPalab[0])
                                gpsTime = subPalab[0];
                                data.gpst=gpsTime
                            if (i == 8):
                                # print("GPS latitude: " + subPalab[0])
                                gpsLatitude = subPalab[0];
                                data.gpsla=gpsLatitude
                            if (i == 9):
                                # print("GPS longitude: " + subPalab[0])
                                gpsLongitude = subPalab[0];
                                data.gpslo=gpsLongitude
                            if (i == 10):
                                # print("GPS Altitude: " + subPalab[0])
                                gpsAltitude = subPalab[0];
                                data.gpsalt=gpsAltitude
                            if (i == 11):
                                # print("GPS Sats: " + subPalab[0])
                                gpsSats = subPalab[0];
                                data.gpssats=gpsSats
                            if (i == 12):
                                # print("Pitch: " + subPalab[0])
                                pitch = subPalab[0];
                                data.pitch=pitch
                            if (i == 13):
                                # print("Roll: " + subPalab[0])
                                roll = subPalab[0];
                                data.roll=roll
                            if (i == 14):
                                # print("Blade Spin rate: " + subPalab[0])
                                bladeSpin = subPalab[0];
                                data.blade=bladeSpin
                            if (i == 15):
                                # print("Software state: " + subPalab[0])
                                softwareState = subPalab[0];
                            if (i == 16):
                                # print("Bonus direction: " + subPalab[0])
                                bonusDirection = subPalab[0];
                            i += 1
    def update():
######################CALCULATE#################
        temp2=float(data.temp)+273.15
        distancia = calculaDistancia(5, 5, float(data.gpsla),float(data.gpslo))
        elevacion = calculaEleva(distancia,float(data.alt))
        azimut = calculaAzimut(5, 5, float(data.gpsla), float(data.gpslo))
        azimutCalib = calculaAzimutCalib(azimut)
        xPos = calculaX(azimut,distancia)
        yPos = calculaY(azimut,distancia)
##########UPDATE FIRST GRAPH######################
        grap1.y.append(float(data.alt))
        #timen=int(data.mtime+1)-(int(data.mtime))
        grap1.x.append(int(data.mtime))
        grap1.curveR.setData(grap1.x, grap1.y)
        grap1.replot()
        grap1.phase += np.pi * 0.02
        grap1.g1title = "Altitude= " + data.alt
        grap1.setTitle(grap1.g1title)
        grap1.counter=grap1.counter+1
##########UPDATE TEXT
        text_pressure.setText("Pressure= "+ str(data.press)+"Pa")
        text_volt.setText("      Voltage= "+ data.volt +"v")
        text_gps_time.setText("GPS Time "+ data.gpst+" s")
        text_gps_la.setText("GPS Latitude= "+ data.gpsla+"°")
        text_gps_lo.setText("GPS Longitude= "+ data.gpslo +"°")
        text_gps_al.setText("GPS Altitude= "+ data.gpsalt+" m")
        text_gps_sats.setText("GPS Sats= "+ data.gpssats)
        text_mission_time.setText("Mission Time= "+ data.mtime)
        text_Packet_count.setText("Packet Count "+ data.packetc +"\n"+' '*75)
        temp_text.setText("Temperature= " + str(round(Decimal(temp2),2))+"K")
        text_elevation.setText("Elevation= "+str(elevacion)+"°")
        text_azimut.setText("Azimut= " + str(azimutCalib))
        text_gs_to_cansat.setText("GS to Cansat= " + str(distancia)+" m")
        text_pitch.setText("Pitch= " + data.pitch +"°")
        text_roll.setText("Roll = " + data.roll + "°")
        text_bladespin.setText("Blade Spin= " + data.blade + " rps")
        text_alt.setText("Altitude= " + data.alt + " rps")
        text_space2.setText(' ' * (round(xPos*0.03+4))*2)
        text_space4.setText('\n ' * ((round(yPos*0.009))-20))
##########UPDATE BAR
        volt_bar.setValue(round(float(data.volt)))
        temp_bar.setValue(temp2)
##########ANGLE
        press=float(data.press)*50
        ang=(0.002685)*press-140
        t = QTransform()
        t.rotate(ang)
        rotated_pixmap = pixmap2.transformed(t, Qt.SmoothTransformation)
        ql1.setPixmap(rotated_pixmap)
###########################################################
        pressp=float(data.blade)*500
        angp=(0.002685)*pressp-140
        print("angulo2")
        print(str(pressp))
        tp = QTransform()
        tp.rotate(angp)
        rotated_pixmapp = pixmap2p.transformed(tp, Qt.SmoothTransformation)
        ql1p.setPixmap(rotated_pixmapp)
        print("update")
##########
    window.show()
    window.setFixedSize(1350, 700)
    timer2 = QTimer()
    timer = QTimer()
    timer2.timeout.connect(serial_connection)
    timer.timeout.connect(update)
    timer.start(1000)
    timer2.start(1)
    app.exec_()