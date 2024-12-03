from Enums.Visualization import Visual
from matplotlib.figure import Figure

class BaseVisual:
    def __init__(self, type:Visual, name:str, supportsFiltering:bool, hasRadio:bool=False):
        self._type = type
        self._name = name
        self._hasFiltering = supportsFiltering
        self._hasRadio = hasRadio
        self._visual = None
        self._data = None

    def set_data(self, data) -> None:
        self._data = data

    def get_data(self):
        return self._data

    def get_id(self) -> Visual:
        return self._type

    def get_name(self) -> str:
        return self._name

    def set_visual(self, visual: Figure) -> None:
        self._visual = visual        

    def get_visual(self) -> Figure:
        return self._visual
    
    def has_filtering(self) -> bool:
        return self._hasFiltering
    
    def has_radio(self) -> bool:
        return self._hasRadio
    
    def create_chart(self) -> None:
        raise NotImplementedError('This method must be implemented in child classes.')
