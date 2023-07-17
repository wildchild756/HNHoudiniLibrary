import hou
import viewerstate.utils as su

class State(object):
    def __init__(self, state_name, scene_viewer):
        self.state_name = state_name
        self.scene_viewer = scene_viewer

    def onEnter(self,kwargs):
        self.scene_viewer.setPromptMessage( 
            'Drop a source file in the viewer', hou.promptMessageType.Prompt )

    def onDragTest( self, kwargs ):
        """ Accept text files only """

        if not hou.ui.hasDragSourceData('text/plain'):
            self.scene_viewer.setPromptMessage( 'Invalid drag drop source', 
                hou.promptMessageType.Error )
            return False

        # note: su.dragSourceFilepath returns the sanitized dragged file path
        su.log(su.dragSourceFilepath())

        return True

    def onDropGetOptions( self, kwargs ):
        """ Populate a drop option list with 3 items """

        kwargs['drop_options']['ids'] = ('option1', 'option2', 'option3')
        kwargs['drop_options']['labels'] = ('Option 1', 'Option 2', 'Option 3')

    def onDropAccept( self, kwargs ):
        """ Process the event with the selected option. """

        su.log( kwargs['drop_selection'] )

        return True  