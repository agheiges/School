
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
def get_model():
	numpy.random.seed(7)
	# load pima indians dataset
	dataset = numpy.loadtxt("wine_train.csv", delimiter=",")
	# split into input (X) and output (Y) variables
	X = dataset[:,1:14]
	Y = dataset[:,0]

	scaler = MinMaxScaler(feature_range=(0, 1))


	thiccX = scaler.fit(transform(x))



	encoder = LabelEncoder()
	encoder.fit(Y)
	encoded_Y = encoder.transform(Y)
	smolY = np_utils.to_categorical(encoded_Y)

	# create model
	model = Sequential()
	model.add(Dense(16, input_dim=13, activation='relu'))
	model.add(Dense(8, activation='sigmoid'))
	model.add(Dense(3, activation='softmax'))


	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	# Fit the model
	model.fit(thiccX, smolY, epochs=150, batch_size=10)
	return model

m = get_model()
scores = m.evaluate(thiccX, smolY)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


