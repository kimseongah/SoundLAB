from keras.models import load_model
from keras.models import model_from_json


model = load_model('model.hdf5')
model.summary()