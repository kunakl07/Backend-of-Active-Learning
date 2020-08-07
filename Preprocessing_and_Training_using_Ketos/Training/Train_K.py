import ketos.data_handling.database_interface as dbi
from ketos.neural_networks.resnet import ResNetInterface
from ketos.data_handling.data_feeding import BatchGenerator


#Transform function to transfrom the input into shape necessary for traning
def transform_batch(X, Y):
  x = X.reshape(X.shape[0],X.shape[1],X.shape[2],1)
  y = tf.one_hot(Y['label'], depth=2, axis=1).numpy()
  return x, y


#Opening the data that is going to be used for traning the model
db = dbi.open_file("/train_database.h5", 'r')
train_data = dbi.open_table(db, "/wav/data")


#Reading the model Recipe
resnet = ResNetInterface.build_from_recipe_file("/recipe.json")


#Extract the train and validation dataset
db2 = dbi.open_file("/train_database.h5", 'r')
train_dataset = dbi.open_table(db2, "/wav/data")
val_dataset = dbi.open_table(db2, "/val3/data")


#Extract the data in batches from the HDF5 files
train_generator = BatchGenerator(batch_size=10, data_table=train_dataset,
                             output_transform_func=ResNetInterface.transform_batch,
                             shuffle=True, refresh_on_epoch_end=True)


val_generator = BatchGenerator(batch_size=10, data_table=val_dataset,
                             output_transform_func=ResNetInterface.transform_batch,
                             shuffle=True, refresh_on_epoch_end=False)



srkw = ResNetInterface.build_from_recipe_file("/recipe.json")

srkw.train_generator = train_generator
srkw.val_generator = val_generator
srkw.checkpoint_dir = "my_checkpoints"
srkw.log_dir = "my_logs"


#Start training
srkw.train_loop(50,validate=True, log_csv=True)