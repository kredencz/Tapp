import os

from PyQt4 import QtCore, QtGui,uic
import maya.cmds as cmds
import maya.OpenMayaUI as omu
import sip

import Tapp.Maya.modelling.utils as mmu

uiPath=os.path.dirname(__file__)+'/resources/triangulatePivot.ui'
#uiPath=r'C:\Users\tokejepsen\Documents\GitHub\Tapp\Tapp\Maya\modelling\GUI\resources/triangulatePivot.ui'
form,base=uic.loadUiType(uiPath)

# MQtUtil class exists in Maya 2011 and up
def maya_main_window():
    ptr = omu.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QtCore.QObject)

class Form(base,form):
    def __init__(self, parent=maya_main_window()):
        super(base,self).__init__(parent)
        self.setupUi(self)
        
        self.setObjectName('triangulatePivot')
        
        self.loadedStyleSheet='QPushButton {color: white;background-color: green}'
        
        self.posVerts=None
        self.upVert=None
    
    def on_loadPositionVerts_pushButton_released(self):
        
        sel=cmds.ls(selection=True,flatten=True)
        
        if len(sel)>0:
            
            shape=cmds.ls(selection=True,objectsOnly=True)[0]
            
            if cmds.nodeType(shape)=='mesh':
                if cmds.polyEvaluate()['vertexComponent']>0:
                
                    verts=[]
                    for vert in sel:
                        
                        verts.append(vert)
                    
                    self.posVerts=verts
                    self.positionVerts_label.setText('Verts loaded!')
                    self.loadPositionVerts_pushButton.setStyleSheet(self.loadedStyleSheet)
                else:
                    cmds.warning('No verts selected!')
            else:
                cmds.warning('Selection is not a vertex!')
        else:
            cmds.warning('Nothing is selected!')
    
    def on_loadUpVert_pushButton_released(self):
        
        sel=cmds.ls(selection=True,flatten=True)
        
        if len(sel)>0:
            
            shape=cmds.ls(selection=True,objectsOnly=True)[0]
            
            if cmds.nodeType(shape)=='mesh':
                if cmds.polyEvaluate()['vertexComponent']>0:
                
                    verts=[]
                    for vert in sel:
                        
                        verts.append(vert)
                    
                    self.upVert=verts
                    self.upVert_label.setText('Vert loaded!')
                    self.loadUpVert_pushButton.setStyleSheet(self.loadedStyleSheet)
                else:
                    cmds.warning('No vert selected!')
            else:
                cmds.warning('Selection is not a vertex!')
        else:
            cmds.warning('Nothing is selected!')
    
    def on_create_pushButton_released(self):
        
        if self.posVerts!=None and self.upVert!=None:
            
            #get check box state
            state=self.locator_checkBox.checkState()
            
            if state==0:
                locatorPivot=False
            if state==2:
                locatorPivot=True
            
            #get check box state
            state=self.mesh_checkBox.checkState()
            
            if state==0:
                meshPivot=False
            if state==2:
                meshPivot=True
            
            #execute
            mmu.triangulatePivot(self.posVerts, self.upVert, locatorPivot, meshPivot)
            
        else:
            cmds.warning('Position Verts and Upvector Vert not loaded!')

def show():
    #closing previous dialog
    for widget in QtGui.qApp.allWidgets():
        if widget.objectName()=='triangulatePivot':
            widget.close()
    
    #showing new dialog
    win=Form()
    win.show()

#show()