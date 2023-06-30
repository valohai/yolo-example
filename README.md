# Valohai YOLO Examples

Welcome to the repository!
This serves as an example showcasing the seamless integration of the [Valohai MLOps platform][vh].
Here, we demonstrate the implementation of [YOLOv5][yl5] with the Valohai platform.
Additionally, we provide insights into utilizing [YOLOv8][yl8] as a library in conjunction with Valohai.

**We've preserved the original YOLO code while leveraging the true magic within the `valohai.yaml` file, where essential configurations are defined.**

We hope this serves as a helpful resource for your MLOps journey!

[yl5]: https://github.com/ultralytics/yolov5/
[yl8]: https://github.com/ultralytics/ultralytics
[vh]: https://valohai.com/

## <div align="center">Installation</div>

Login to the [Valohai app][app] and create a new project.

### Configure the repository:

<details open>
<summary>Using UI</summary>

Configure this repository as the project's repository, by following these steps:

1. Go to your project's page.
2. Navigate to the Settings tab.
3. Under the Repository section, locate the URL field.
4. Enter the URL of this repository.
5. Click on the Save button to save the changes.
</details>

<details open>
<summary>Using terminal</summary>

To run your code on Valohai using the terminal, follow these steps:

1. Install Valohai on your machine by running the following command:

```bash
pip install valohai-cli valohai-utils
```

2. Log in to Valohai from the terminal using the command:

```bash
vh login
```

3. Create a project for your Valohai workflow.
   Start by creating a directory for your project:

```bash
mkdir valohai-yolo-example
cd valohai-yolo-example
```

Then, create the Valohai project:

```bash
vh project create
```

4. Clone the repository to your local machine:

```bash
git clone https://github.com/valohai/yolo-example.git .
```

</details>

Now you are ready to run executions and pipelines.

## <div align="center">Running Executions</div>

This repository covers essential tasks such as training, prediction, and evaluation using YOLOv5 and YOLOv5-seg models.
Additionally, we provide the [Ultralytics example][v8exmpl] demonstrating the usage of YOLOv8 with Valohai, including training, evaluation, prediction, and ONNX exporting.

<details open>
<summary>Using UI</summary>

1. Go to the Executions tab in your project.
2. Create a new execution by selecting the predefined steps: _train-yolov5, predict-yolov5, validate-yolov5, train-seg-yolov5, predict-seg-yolov5, validate-seg-yolov5, run-yolov8._
3. Customize the execution parameters if needed.
4. Start the execution to run the selected step.

![alt text](https://github.com/valohai/yolo-example/blob/master/screenshots/ui_create_execution.jpg)

</details>

<details open>
<summary>Using terminal</summary>

To run individual steps, execute the following command:

```bash
vh execution run <step-name> --adhoc
```

For example, to run the preprocess-dataset step, use the command:

```bash
vh execution run train-yolov5 --adhoc
```

You can also set parameters for your execution (see what paramenters you can set in `valohai.yaml`):

```bash
vh execution run train-yolov5 --epochs=10 --adhoc
```

</details>

## <div align="center">Running Pipeline</div>

<details open>
<summary>Using UI</summary>

1. Navigate to the Pipelines tab.
2. Create a new pipeline and select out pipeline called _train-val-pipeline-yolov5_.
3. Configure the pipeline settings.
4. Start the pipeline.

![alt text](https://github.com/valohai/yolo-example/blob/master/screenshots/ui_create_pipeline.jpg)

</details>

<details open>
<summary>Using terminal</summary>

To run pipelines, use the following command:

```bash
vh pipeline run <pipeline-name> --adhoc
```

For example, to run our pipeline, use the command:

```bash
vh pipeline run train-val-pipeline-yolov5 --adhoc
```

</details>

## <div align="center">Results & Visualizations</div>

During the execution of the code, you can monitor the graphs generated with the metadata.
Additionally, once the execution is complete, you can access the output files containing the results.

### Results examples

<p float="left">
<img src="https://github.com/valohai/yolo-example/blob/master/screenshots/results_val_obj_detection.jpg" width="412" height="412">
<img src="https://github.com/valohai/yolo-example/blob/master/screenshots/results_val_segmentation.jpg" width="412" height="412">
</p>
 
### Evaluation example

<img src="https://github.com/valohai/yolo-example/blob/master/screenshots/results_p_curve.jpg" width="512" height="512">

### Generated Metadata graph

![alt text](https://github.com/valohai/yolo-example/blob/master/screenshots/results_metadata_graph.jpg)

## <div align="center">Dataset Management</div>

### Configuring Dataset Path with coco128.yaml

To ensure the integrity of the original YOLOv5 repository, we decided not to modify it.
However, we needed to connect the dataset to our S3 bucket by adjusting the file path.

We created our own version of the coco128.yaml file named `datasets/coco128.yaml` and `datasets/coco128-seg.yaml` for segmentation.

In this customized YAML files, we set the dataset path to `/valohai/repository/coco128/` and `/valohai/repository/coco128-seg/`.

### Utilizing Valohai Inputs for Dataset Integration

To streamline the process, we made use of **Valohai inputs.**

Configuring the `valohai.yaml` file, we defined default input datasets that include the link to our S3 bucket.

When executing the code, Valohai automatically handles the downloading and caching of the dataset, ensuring seamless integration with our workflow.

### Utilizing Archived Dataset

In order to make this repository accessible to all Valohai users, we have utilized a .tar dataset instead of a wildcard with the S3 bucket. This decision was made because public S3 buckets do not support wildcard functionality.

Therefore, in the `valohai.yaml` file, you will notice that we use the link to `coco128.tar` file as the default dataset input and employ the tar command (`tar -xf /valohai/inputs/datasets/coco128.tar`) in the command section to extract the dataset.

### Utilizing private S3 bucket wildcard

1. Create your own S3 bucket. [Follow these steps.][s3]
2. Upload your dataset to the S3 bucket.
3. Add S3 bucket to your Data Store. To include an S3 bucket as your Data Store, navigate to the project's settings, then select Data Stores.
   From there, you can add a new store by choosing Amazon S3.
4. Set the link to your S3 bucket as the default dataset in `valohai.yaml`, add it to the inputs section of the relevant step. 
Which should look like this: `s3://data-yolov5/datasets/coco128/*`
5. Change the link to dataset in `datasets/coco128.yaml` file. Set `path:/valohai/inputs/datasets/`

6. Delete the `tar -xf /valohai/inputs/datasets/coco128.tar` from command section in `valohai.yaml`

![alt text](https://github.com/valohai/yolo-example/blob/master/screenshots/add_s3_bucket.jpg)

## <div align="center">Valohai_watch</div>

The _valohai_watch.py_ script is a valuable tool for monitoring the results of a training process while the code is still running. It serves several purposes:

- Continuous Observation: The script utilizes the **watchdog** library to continuously monitor a specified directory for changes.
  This enables real-time observation of the evolving results of your training.

- CSV to JSON Conversion: The script reads and extracts metadata, when CSV files are modified.
  This metadata is converted to JSON, enabling us to create visualizations such as charts or graphs on the Valohai page.

Overall, we use valohai_watch to convert training, testing, and validation metadata into a format that Valohai can read.
While Valohai doesn't usually need monitoring scripts, we included this example to show how it works without changing the original YOLO code.

## <div align="center">Contact</div>

For bug reports and feature requests please visit GitHub Issues.

[app]: https://app.valohai.com
[s3]: https://help.valohai.com/hc/en-us/articles/4421421651729-Configure-an-AWS-S3-Bucket
[v8exmpl]: https://docs.ultralytics.com/usage/python/
