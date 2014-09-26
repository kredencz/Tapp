#
#    ngSkinTools
#    Copyright (c) 2009-2013 Viktoras Makauskas. 
#    All rights reserved.
#    
#    Get more information at 
#        http://www.ngskintools.com
#        http://www.neglostyti.com
#    
#    --------------------------------------------------------------------------
#
#    The coded instructions, statements, computer programs, and/or related
#    material (collectively the "Data") in these files are subject to the terms 
#    and conditions defined by
#    Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License:
#        http://creativecommons.org/licenses/by-nc-nd/3.0/
#        http://creativecommons.org/licenses/by-nc-nd/3.0/legalcode
#        http://creativecommons.org/licenses/by-nc-nd/3.0/legalcode.txt
#         
#    A copy of the license can be found in file 'LICENSE.txt', which is part 
#    of this source code package.
#    

from ngSkinTools.utils import Utils
from maya import cmds


class Signal:
    '''
    Signal class collects observers, interested in some particular event,and handles
    signaling them all when some event occurs. Both handling and signaling happens outside
    of signal's own code
    '''
    
    TOTAL_HANDLERS = 0
    
    def __init__(self,name=None):
        self.name = name
        self.reset();
        
    def reset(self):
        self.handlers = []
        self.executing = False
        
    
    def emitDeffered(self,*args):
        import maya.utils as mu
        mu.executeDeferred(self.emit,*args)
        
        
    def emit(self,*args):
        if self.executing:
            raise Exception,'Nested emit on %s detected' % self.name
        
        self.executing = True
        try:
            for i in self.handlers:
                i(*args)
        finally:
            self.executing = False
            

    class UiBoundHandler:
        '''
        Proxy wrapper for event handlers that has a method to deactivate 
        itself after when associated UI is deleted
        '''
        def __init__(self,handler,ownerUI,deactivateHandler):
            cmds.scriptJob(uiDeleted=[ownerUI,self.deactivate])
            self.handler=handler
            self.deactivateHandler=deactivateHandler
        
        def deactivate(self):
            self.deactivateHandler(self)
            
            
        def __call__(self):
            self.handler()
            
            
    def addHandler(self,handler,ownerUI=None):
        # if there's owning UI, wrap everything into self-deactivating handler
        if (ownerUI!=None):
            handler=self.UiBoundHandler(handler,ownerUI,self.removeHandler)
            
        self.handlers.append(handler)

    def removeHandler(self,handler):
        self.handlers.remove(handler)
        


class EventsHost(object):
    def restart(self):
        for _, propertyValue in vars(self).iteritems():
            if isinstance(propertyValue, Signal):
                propertyValue.reset()

class LayerEventsHost(EventsHost):
    """
    layer system related events
    """
    
    def __init__(self):
        self.nameChanged = Signal('layerNameChanged')
        self.layerListModified = Signal('layerDataModified')
        self.currentLayerChanged = Signal('currentLayerChanged')
        self.currentInfluenceChanged = Signal('currentInfluenceChanged')
        self.layerSelectionChanged = Signal('layerSelectionChanged')
        self.layerListUpdated = Signal('layerListUpdated')
        self.layerAvailabilityChanged = Signal('layerAvailabilityChanged')
        self.influenceListChanged = Signal('influenceListChanged')
        self.mirrorCacheStatusChanged = Signal('mirrorCacheStatusChanged')


class MayaEventsHost(EventsHost):
    '''
    global maya-specific events
    '''
    def __init__(self):
        self.scriptJobs = []
        
        self.nodeSelectionChanged = Signal('nodeSelectionChanged')
        self.undoRedoExecuted = Signal('undoRedoExecuted')
        self.toolChanged = Signal('toolChanged')
        self.quitApplication = Signal('quitApplication')
        
    def registerScriptJob(self,jobName,handler):
        job = cmds.scriptJob(e=[jobName,handler])
        self.scriptJobs.append(job)
        
    def deregisterScriptJobs(self):
        for i in self.scriptJobs:
            cmds.scriptJob(kill=i)
        self.scriptJobs = []
            
    def registerScriptJobs(self):
        self.registerScriptJob('SelectionChanged',self.nodeSelectionChanged.emit)
        self.registerScriptJob('Undo',self.undoRedoExecuted.emit)
        self.registerScriptJob('Redo',self.undoRedoExecuted.emit)
        self.registerScriptJob('ToolChanged',self.toolChanged.emit)        
        self.registerScriptJob('quitApplication',self.quitApplication.emit)    
        
    
    


def restartEvents():
    '''
    (re)creates signal holders in LayerEvents and MayaEvents  
    '''
    MayaEvents.restart()
    LayerEvents.restart()


MayaEvents = MayaEventsHost()
LayerEvents = LayerEventsHost() 
