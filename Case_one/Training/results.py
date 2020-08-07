import logging
import argparse
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from matplotlib import pyplot
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import f1_score
from sklearn.metrics import auc

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def  plot_roc_curve(test_path, model_path):
    """ Plotting the ROC curve."""
    img_width, img_height = 607, 617
    test_data_path = test_path

    test_generator = ImageDataGenerator()
    test_data_generator = test_generator.flow_from_directory(
        test_data_path,
        target_size=(img_width, img_height),
        batch_size=32,
        shuffle=False)
    test_steps_per_epoch = np.math.ceil(
        test_data_generator.samples /
        test_data_generator.batch_size)

    model = load_model(model_path)

    predictions = model.predict_generator(
        test_data_generator, steps=test_steps_per_epoch)
    predictions[predictions <= 0.5] = 0
    predictions[predictions > 0.5] = 1

    predicted_classes = (predictions).astype(np.int)

    true_classes = test_data_generator.classes
    ns_probs = [0 for _ in range(len(predicted_classes[:, 0]))]
    # calculate scores
    ns_auc = roc_auc_score(predicted_classes[:, 0], ns_probs)
    lr_auc = roc_auc_score(predicted_classes[:, 0], true_classes)
    # summarize scores
    print('No Skill: ROC AUC=%.3f' % (ns_auc))
    print('Logistic: ROC AUC=%.3f' % (lr_auc))
    #   calculate roc curves
    ns_fpr, ns_tpr, _ = roc_curve(predictions[:, 0], ns_probs)
    lr_fpr, lr_tpr, _ = roc_curve(predictions[:, 0], true_classes)
    # plot the roc curve for the model
    pyplot.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')
    pyplot.plot(lr_fpr, lr_tpr, marker='.', label='Logistic')
    # axis labels
    pyplot.xlabel('False Positive Rate')
    pyplot.ylabel('True Positive Rate')
    # show the legend
    pyplot.legend()
    # show the plot
    pyplot.show()


def precision_recall_curve(model_path, test_path):
    """ Plotting the precision_recall_graph """
    img_width, img_height = 607, 617
    test_data_path = test_path

    test_generator = ImageDataGenerator()
    test_data_generator = test_generator.flow_from_directory(
        test_data_path,
        target_size=(img_width, img_height),
        batch_size=32,
        shuffle=False)
    test_steps_per_epoch = np.math.ceil(
        test_data_generator.samples /
        test_data_generator.batch_size)

    model = load_model(model_path)

    predictions = model.predict_generator(
        test_data_generator, steps=test_steps_per_epoch)
    predictions[predictions <= 0.5] = 0
    predictions[predictions > 0.5] = 1

    predicted_classes = (predictions).astype(np.int)

    true_classes = test_data_generator.classes
    class_labels = list(test_data_generator.class_indices.keys())
    lr_precision, lr_recall, _ = precision_recall_curve(true_classes, predictions[:,0])
    lr_f1, lr_auc = f1_score(true_classes, predictions[:,0]), auc(lr_recall, lr_precision)
    # summarize scores
    print('Logistic: f1=%.3f auc=%.3f' % (lr_f1, lr_auc))
    # plot the precision-recall curves
    no_skill = len(true_classes[true_classes==1]) / len(true_classes)
    pyplot.plot([0, 1], [no_skill, no_skill], linestyle='--', label='No Skill')
    pyplot.plot(lr_recall, lr_precision, marker='.', label='Logistic')
    # axis labels
    pyplot.xlabel('Recall')
    pyplot.ylabel('Precision')
    # show the legend
    pyplot.legend()
    # show the plot
    pyplot.show()

def classification_report_sklearn(model_path, test_path):
    '''Print Classification report from sklearn'''
    img_width, img_height =  607, 617
    test_data_path = test_path

    test_generator = ImageDataGenerator()
    test_data_generator = test_generator.flow_from_directory(
        test_data_path,
        target_size=(img_width, img_height),
        batch_size=32,
        shuffle=False)
    test_steps_per_epoch = np.math.ceil(
        test_data_generator.samples /
        test_data_generator.batch_size)

    model = load_model(model_path)

    predictions = model.predict_generator(
        test_data_generator, steps=test_steps_per_epoch)
    predictions[predictions <= 0.5] = 0
    predictions[predictions > 0.5] = 1

    predicted_classes = (predictions).astype(np.int)

    true_classes = test_data_generator.classes
    class_labels = list(test_data_generator.class_indices.keys())

    report = metrics.classification_report(
        true_classes, predicted_classes, target_names=class_labels)
    print(report)

    cm = confusion_matrix(true_classes, predicted_classes)
    total = sum(sum(cm))
    acc = (cm[0, 0] + cm[1, 1]) / total
    sensitivity = cm[0, 0] / (cm[0, 0] + cm[0, 1])
    specificity = cm[1, 1] / (cm[1, 0] + cm[1, 1])

    # show the confusion matrix, accuracy, sensitivity, and specificity
    print(cm)
    print("Accuracy: {:.4f}".format(acc))
    print("Sensitivity: {:.4f}".format(sensitivity))
    print("Specificity: {:.4f}".format(specificity))


def main(args):
    model_path = args.modelpath
    test_path = args.testpath

    classification_report_sklearn(model_path, test_path)
    plot_roc_curve(model_path, test_path)
    precision_recall_curve(model_path, test_path)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Predict which images are orcas")
    parser.add_argument(
        '-m',
        '--modelpath',
        type=str,
        help='path to saved model weights',
        required=True)
    parser.add_argument(
        '-c',
        "--testpath",
        type=str,
        help='directory with Test images',
        required=True)

    args = parser.parse_args()

    main(args)