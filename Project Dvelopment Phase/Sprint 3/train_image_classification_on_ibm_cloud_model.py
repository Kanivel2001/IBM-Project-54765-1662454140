# -*- coding: utf-8 -*-
"""Train image classification on IBM cloud model

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M8swRzEuerTlr_g4szlkqnjZUyc-YkOM
"""

!pip install watson-machine-learning-client
Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/
Collecting watson-machine-learning-client
  Downloading watson_machine_learning_client-1.0.391-py3-none-any.whl (538 kB)
     |████████████████████████████████| 538 kB 12.3 MB/s 
Requirement already satisfied: tqdm in /usr/local/lib/python3.7/dist-packages (from watson-machine-learning-client) (4.64.1)
Requirement already satisfied: requests in /usr/local/lib/python3.7/dist-packages (from watson-machine-learning-client) (2.23.0)
Requirement already satisfied: urllib3 in /usr/local/lib/python3.7/dist-packages (from watson-machine-learning-client) (1.24.3)
Requirement already satisfied: pandas in /usr/local/lib/python3.7/dist-packages (from watson-machine-learning-client) (1.3.5)
Requirement already satisfied: certifi in /usr/local/lib/python3.7/dist-packages (from watson-machine-learning-client) (2022.9.24)
Collecting ibm-cos-sdk
  Downloading ibm-cos-sdk-2.12.0.tar.gz (55 kB)
     |████████████████████████████████| 55 kB 4.2 MB/s 
Collecting lomond
  Downloading lomond-0.3.3-py2.py3-none-any.whl (35 kB)
Collecting boto3
  Downloading boto3-1.26.7-py3-none-any.whl (132 kB)
     |████████████████████████████████| 132 kB 61.1 MB/s 
Requirement already satisfied: tabulate in /usr/local/lib/python3.7/dist-packages (from watson-machine-learning-client) (0.8.10)
Collecting botocore<1.30.0,>=1.29.7
  Downloading botocore-1.29.7-py3-none-any.whl (9.9 MB)
     |████████████████████████████████| 9.9 MB 57.9 MB/s 
Collecting s3transfer<0.7.0,>=0.6.0
  Downloading s3transfer-0.6.0-py3-none-any.whl (79 kB)
     |████████████████████████████████| 79 kB 7.1 MB/s 
Collecting jmespath<2.0.0,>=0.7.1
  Downloading jmespath-1.0.1-py3-none-any.whl (20 kB)
Collecting urllib3
  Downloading urllib3-1.26.12-py2.py3-none-any.whl (140 kB)
     |████████████████████████████████| 140 kB 82.1 MB/s 
Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in /usr/local/lib/python3.7/dist-packages (from botocore<1.30.0,>=1.29.7->boto3->watson-machine-learning-client) (2.8.2)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/dist-packages (from python-dateutil<3.0.0,>=2.1->botocore<1.30.0,>=1.29.7->boto3->watson-machine-learning-client) (1.15.0)
Collecting ibm-cos-sdk-core==2.12.0
  Downloading ibm-cos-sdk-core-2.12.0.tar.gz (956 kB)
     |████████████████████████████████| 956 kB 64.0 MB/s 
Collecting ibm-cos-sdk-s3transfer==2.12.0
  Downloading ibm-cos-sdk-s3transfer-2.12.0.tar.gz (135 kB)
     |████████████████████████████████| 135 kB 58.9 MB/s 
Collecting jmespath<2.0.0,>=0.7.1
  Downloading jmespath-0.10.0-py2.py3-none-any.whl (24 kB)
Collecting requests
  Downloading requests-2.28.1-py3-none-any.whl (62 kB)
     |████████████████████████████████| 62 kB 1.2 MB/s 
Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests->watson-machine-learning-client) (2.10)
Requirement already satisfied: charset-normalizer<3,>=2 in /usr/local/lib/python3.7/dist-packages (from requests->watson-machine-learning-client) (2.1.1)
Requirement already satisfied: numpy>=1.17.3 in /usr/local/lib/python3.7/dist-packages (from pandas->watson-machine-learning-client) (1.21.6)
Requirement already satisfied: pytz>=2017.3 in /usr/local/lib/python3.7/dist-packages (from pandas->watson-machine-learning-client) (2022.6)
Building wheels for collected packages: ibm-cos-sdk, ibm-cos-sdk-core, ibm-cos-sdk-s3transfer
  Building wheel for ibm-cos-sdk (setup.py) ... done
  Created wheel for ibm-cos-sdk: filename=ibm_cos_sdk-2.12.0-py3-none-any.whl size=73931 sha256=7bb6d15b2a608d3d4657e6b5ba98f74ab002a084e180020f3a1f0213cba0bf37
  Stored in directory: /root/.cache/pip/wheels/ec/94/29/2b57327cf00664b6614304f7958abd29d77ea0e5bbece2ea57
  Building wheel for ibm-cos-sdk-core (setup.py) ... done
  Created wheel for ibm-cos-sdk-core: filename=ibm_cos_sdk_core-2.12.0-py3-none-any.whl size=562962 sha256=1ee48cb7c85b75e505b11fca14d7dece0ff88d8c6ed47d5d893a61e8a8e5fe94
  Stored in directory: /root/.cache/pip/wheels/64/56/fb/5cd6f4f40406c828a5289b95b2752a4d142a9afb359244ed8d
  Building wheel for ibm-cos-sdk-s3transfer (setup.py) ... done
  Created wheel for ibm-cos-sdk-s3transfer: filename=ibm_cos_sdk_s3transfer-2.12.0-py3-none-any.whl size=89778 sha256=706652096c1249f97be1d9ec1bfcafcc3224e10007fcba01a94bcf227043ab5f
  Stored in directory: /root/.cache/pip/wheels/57/79/6a/ffe3370ed7ebc00604f9f76766e1e0348dcdcad2b2e32df9e1
Successfully built ibm-cos-sdk ibm-cos-sdk-core ibm-cos-sdk-s3transfer
Installing collected packages: urllib3, requests, jmespath, ibm-cos-sdk-core, botocore, s3transfer, ibm-cos-sdk-s3transfer, lomond, ibm-cos-sdk, boto3, watson-machine-learning-client
  Attempting uninstall: urllib3
    Found existing installation: urllib3 1.24.3
    Uninstalling urllib3-1.24.3:
      Successfully uninstalled urllib3-1.24.3
  Attempting uninstall: requests
    Found existing installation: requests 2.23.0
    Uninstalling requests-2.23.0:
      Successfully uninstalled requests-2.23.0
Successfully installed boto3-1.26.7 botocore-1.29.7 ibm-cos-sdk-2.12.0 ibm-cos-sdk-core-2.12.0 ibm-cos-sdk-s3transfer-2.12.0 jmespath-0.10.0 lomond-0.3.3 requests-2.28.1 s3transfer-0.6.0 urllib3-1.26.12 watson-machine-learning-client-1.0.391
!pip install ibm_watson_machine_learning
Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/
Collecting ibm_watson_machine_learning
  Downloading ibm_watson_machine_learning-1.0.257-py3-none-any.whl (1.8 MB)
     |████████████████████████████████| 1.8 MB 12.5 MB/s 
Requirement already satisfied: lomond in /usr/local/lib/python3.7/dist-packages (from ibm_watson_machine_learning) (0.3.3)
Requirement already satisfied: tabulate in /usr/local/lib/python3.7/dist-packages (from ibm_watson_machine_learning) (0.8.10)
Requirement already satisfied: pandas<1.5.0,>=0.24.2 in /usr/local/lib/python3.7/dist-packages (from ibm_watson_machine_learning) (1.3.5)
Requirement already satisfied: certifi in /usr/local/lib/python3.7/dist-packages (from ibm_watson_machine_learning) (2022.9.24)
Requirement already satisfied: packaging in /usr/local/lib/python3.7/dist-packages (from ibm_watson_machine_learning) (21.3)
Requirement already satisfied: importlib-metadata in /usr/local/lib/python3.7/dist-packages (from ibm_watson_machine_learning) (4.13.0)
Requirement already satisfied: urllib3 in /usr/local/lib/python3.7/dist-packages (from ibm_watson_machine_learning) (1.26.12)
Requirement already satisfied: requests in /usr/local/lib/python3.7/dist-packages (from ibm_watson_machine_learning) (2.28.1)
Collecting ibm-cos-sdk==2.7.*
  Downloading ibm-cos-sdk-2.7.0.tar.gz (51 kB)
     |████████████████████████████████| 51 kB 562 kB/s 
Collecting ibm-cos-sdk-core==2.7.0
  Downloading ibm-cos-sdk-core-2.7.0.tar.gz (824 kB)
     |████████████████████████████████| 824 kB 47.4 MB/s 
Collecting ibm-cos-sdk-s3transfer==2.7.0
  Downloading ibm-cos-sdk-s3transfer-2.7.0.tar.gz (133 kB)
     |████████████████████████████████| 133 kB 72.5 MB/s 
Requirement already satisfied: jmespath<1.0.0,>=0.7.1 in /usr/local/lib/python3.7/dist-packages (from ibm-cos-sdk==2.7.*->ibm_watson_machine_learning) (0.10.0)
Collecting docutils<0.16,>=0.10
  Downloading docutils-0.15.2-py3-none-any.whl (547 kB)
     |████████████████████████████████| 547 kB 72.5 MB/s 
Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in /usr/local/lib/python3.7/dist-packages (from ibm-cos-sdk-core==2.7.0->ibm-cos-sdk==2.7.*->ibm_watson_machine_learning) (2.8.2)
Requirement already satisfied: pytz>=2017.3 in /usr/local/lib/python3.7/dist-packages (from pandas<1.5.0,>=0.24.2->ibm_watson_machine_learning) (2022.6)
Requirement already satisfied: numpy>=1.17.3 in /usr/local/lib/python3.7/dist-packages (from pandas<1.5.0,>=0.24.2->ibm_watson_machine_learning) (1.21.6)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/dist-packages (from python-dateutil<3.0.0,>=2.1->ibm-cos-sdk-core==2.7.0->ibm-cos-sdk==2.7.*->ibm_watson_machine_learning) (1.15.0)
Requirement already satisfied: charset-normalizer<3,>=2 in /usr/local/lib/python3.7/dist-packages (from requests->ibm_watson_machine_learning) (2.1.1)
Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests->ibm_watson_machine_learning) (2.10)
Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata->ibm_watson_machine_learning) (3.10.0)
Requirement already satisfied: typing-extensions>=3.6.4 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata->ibm_watson_machine_learning) (4.1.1)
Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from packaging->ibm_watson_machine_learning) (3.0.9)
Building wheels for collected packages: ibm-cos-sdk, ibm-cos-sdk-core, ibm-cos-sdk-s3transfer
  Building wheel for ibm-cos-sdk (setup.py) ... done
  Created wheel for ibm-cos-sdk: filename=ibm_cos_sdk-2.7.0-py2.py3-none-any.whl size=72563 sha256=82b87c6ecc3373656ab6f3022e47f1184a879f9604adece00255929c0f0ac90d
  Stored in directory: /root/.cache/pip/wheels/47/22/bf/e1154ff0f5de93cc477acd0ca69abfbb8b799c5b28a66b44c2
  Building wheel for ibm-cos-sdk-core (setup.py) ... done
  Created wheel for ibm-cos-sdk-core: filename=ibm_cos_sdk_core-2.7.0-py2.py3-none-any.whl size=501013 sha256=ab7a7e33ae17a0db11e44a904b9ab2a8d088491f1149868eb4d1e7ba0f4a32de
  Stored in directory: /root/.cache/pip/wheels/6c/a2/e4/c16d02f809a3ea998e17cfd02c13369281f3d232aaf5902c19
  Building wheel for ibm-cos-sdk-s3transfer (setup.py) ... done
  Created wheel for ibm-cos-sdk-s3transfer: filename=ibm_cos_sdk_s3transfer-2.7.0-py2.py3-none-any.whl size=88622 sha256=e6e47f580ebf120cd0d496be94e8c6c5d4576a34da3be86eb6dfe2c2ec51634d
  Stored in directory: /root/.cache/pip/wheels/5f/b7/14/fbe02bc1ef1af890650c7e51743d1c83890852e598d164b9da
Successfully built ibm-cos-sdk ibm-cos-sdk-core ibm-cos-sdk-s3transfer
Installing collected packages: docutils, ibm-cos-sdk-core, ibm-cos-sdk-s3transfer, ibm-cos-sdk, ibm-watson-machine-learning
  Attempting uninstall: docutils
    Found existing installation: docutils 0.17.1
    Uninstalling docutils-0.17.1:
      Successfully uninstalled docutils-0.17.1
  Attempting uninstall: ibm-cos-sdk-core
    Found existing installation: ibm-cos-sdk-core 2.12.0
    Uninstalling ibm-cos-sdk-core-2.12.0:
      Successfully uninstalled ibm-cos-sdk-core-2.12.0
  Attempting uninstall: ibm-cos-sdk-s3transfer
    Found existing installation: ibm-cos-sdk-s3transfer 2.12.0
    Uninstalling ibm-cos-sdk-s3transfer-2.12.0:
      Successfully uninstalled ibm-cos-sdk-s3transfer-2.12.0
  Attempting uninstall: ibm-cos-sdk
    Found existing installation: ibm-cos-sdk 2.12.0
    Uninstalling ibm-cos-sdk-2.12.0:
      Successfully uninstalled ibm-cos-sdk-2.12.0
Successfully installed docutils-0.15.2 ibm-cos-sdk-2.7.0 ibm-cos-sdk-core-2.7.0 ibm-cos-sdk-s3transfer-2.7.0 ibm-watson-machine-learning-1.0.257
#Connecting to IBM Cloud from Notebook
from ibm_watson_machine_learning import APIClient
credentials = {
    'url':'https://eu-gb.ml.cloud.ibm.com',
    'apikey':"IPJl2muoiEQuiCN8SlAVWhibUleKXXfaBLhsV1BqG13F"
}
Client = APIClient(credentials)
Python 3.7 and 3.8 frameworks are deprecated and will be removed in a future release. Use Python 3.9 framework instead.
Client
Client.spaces.get_details()
{'resources': [{'entity': {'compute': [{'crn': 'crn:v1:bluemix:public:pm-20:eu-gb:a/942b74057f4f4693a5063e53a1998c0a:fd4c34ac-8fb8-4091-803e-702fd69e7268::',
      'guid': 'fd4c34ac-8fb8-4091-803e-702fd69e7268',
      'name': 'Watson Machine Learning-np',
      'type': 'machine_learning'}],
    'description': '',
    'name': 'FFD_DEPLOYMENT',
    'scope': {'bss_account_id': '942b74057f4f4693a5063e53a1998c0a'},
    'stage': {'production': False},
    'status': {'state': 'active'},
    'storage': {'properties': {'bucket_name': '40eacea5-8669-4880-9cfa-020f7b937fd4',
      'bucket_region': 'eu-gb-standard',
      'credentials': {'admin': {'access_key_id': '58823ca22e35459f9ed23e5b64c52395',
        'api_key': 'sVpdNRV_kFC_io-UFrygUfCvKG73HUFzg6klpZTdATir',
        'secret_access_key': '7a4d123516809989ff6335da34b75262f8d1b2720b1e3993',
        'service_id': 'ServiceId-487cda5f-c257-41ec-91b1-3676d0a722ec'},
       'editor': {'access_key_id': '11c6512f22854163bdaeeaad7c6e634f',
        'api_key': 'GEk5XKTAgI4ksFK3rCYNOdoOrITNeeZ9PAgU_hnADMc0',
        'resource_key_crn': 'crn:v1:bluemix:public:cloud-object-storage:global:a/942b74057f4f4693a5063e53a1998c0a:b78a8b79-a65e-42a3-ac79-d321809c7229::',
        'secret_access_key': 'c2da1f5c3c59a1dd9281f5f70452054b9ee9ed51ada007a9',
        'service_id': 'ServiceId-c50c41ba-8112-4602-bd81-898d2c342031'},
       'viewer': {'access_key_id': 'ffc7eb706a6a41b886114b0a6a379f9b',
        'api_key': '7TwTkdvDMxsOLwSrclwGYq-hVjQPQisRmfb32p46tykQ',
        'resource_key_crn': 'crn:v1:bluemix:public:cloud-object-storage:global:a/942b74057f4f4693a5063e53a1998c0a:b78a8b79-a65e-42a3-ac79-d321809c7229::',
        'secret_access_key': '6c0bccf003e873a5537a320adef6e931cfadc716784354af',
        'service_id': 'ServiceId-bde18ae1-9a35-4d2a-aeee-874fcb6c31d1'}},
      'endpoint_url': 'https://s3.eu-gb.cloud-object-storage.appdomain.cloud',
      'guid': 'b78a8b79-a65e-42a3-ac79-d321809c7229',
      'resource_crn': 'crn:v1:bluemix:public:cloud-object-storage:global:a/942b74057f4f4693a5063e53a1998c0a:b78a8b79-a65e-42a3-ac79-d321809c7229::'},
     'type': 'bmcos_object_storage'}},
   'metadata': {'created_at': '2022-11-11T20:38:20.212Z',
    'creator_id': 'IBMid-66100457F5',
    'id': '54f66e28-7d03-4808-8e64-b0c3b4826004',
    'updated_at': '2022-11-11T20:38:37.758Z',
    'url': '/v2/spaces/54f66e28-7d03-4808-8e64-b0c3b4826004'}}]}
Client.spaces.list()
Note: 'limit' is not provided. Only first 50 records will be displayed if the number of records exceed 50
------------------------------------  --------------  ------------------------
ID                                    NAME            CREATED
54f66e28-7d03-4808-8e64-b0c3b4826004  FFD_DEPLOYMENT  2022-11-11T20:38:20.212Z
------------------------------------  --------------  ------------------------
space_uid = '54f66e28-7d03-4808-8e64-b0c3b4826004' #Space User ID
space_uid
'54f66e28-7d03-4808-8e64-b0c3b4826004'
#Setting created deployment space as default
Client.set.default_space(space_uid)
'SUCCESS'
#Seeing tensorflow asset_id
Client.software_specifications.list()
-----------------------------  ------------------------------------  ----
NAME                           ASSET_ID                              TYPE
default_py3.6                  0062b8c9-8b7d-44a0-a9b9-46c416adcbd9  base
kernel-spark3.2-scala2.12      020d69ce-7ac1-5e68-ac1a-31189867356a  base
pytorch-onnx_1.3-py3.7-edt     069ea134-3346-5748-b513-49120e15d288  base
scikit-learn_0.20-py3.6        09c5a1d0-9c1e-4473-a344-eb7b665ff687  base
spark-mllib_3.0-scala_2.12     09f4cff0-90a7-5899-b9ed-1ef348aebdee  base
pytorch-onnx_rt22.1-py3.9      0b848dd4-e681-5599-be41-b5f6fccc6471  base
ai-function_0.1-py3.6          0cdb0f1e-5376-4f4d-92dd-da3b69aa9bda  base
shiny-r3.6                     0e6e79df-875e-4f24-8ae9-62dcc2148306  base
tensorflow_2.4-py3.7-horovod   1092590a-307d-563d-9b62-4eb7d64b3f22  base
pytorch_1.1-py3.6              10ac12d6-6b30-4ccd-8392-3e922c096a92  base
tensorflow_1.15-py3.6-ddl      111e41b3-de2d-5422-a4d6-bf776828c4b7  base
autoai-kb_rt22.2-py3.10        125b6d9a-5b1f-5e8d-972a-b251688ccf40  base
runtime-22.1-py3.9             12b83a17-24d8-5082-900f-0ab31fbfd3cb  base
scikit-learn_0.22-py3.6        154010fa-5b3b-4ac1-82af-4d5ee5abbc85  base
default_r3.6                   1b70aec3-ab34-4b87-8aa0-a4a3c8296a36  base
pytorch-onnx_1.3-py3.6         1bc6029a-cc97-56da-b8e0-39c3880dbbe7  base
kernel-spark3.3-r3.6           1c9e5454-f216-59dd-a20e-474a5cdf5988  base
pytorch-onnx_rt22.1-py3.9-edt  1d362186-7ad5-5b59-8b6c-9d0880bde37f  base
tensorflow_2.1-py3.6           1eb25b84-d6ed-5dde-b6a5-3fbdf1665666  base
spark-mllib_3.2                20047f72-0a98-58c7-9ff5-a77b012eb8f5  base
tensorflow_2.4-py3.8-horovod   217c16f6-178f-56bf-824a-b19f20564c49  base
runtime-22.1-py3.9-cuda        26215f05-08c3-5a41-a1b0-da66306ce658  base
do_py3.8                       295addb5-9ef9-547e-9bf4-92ae3563e720  base
autoai-ts_3.8-py3.8            2aa0c932-798f-5ae9-abd6-15e0c2402fb5  base
tensorflow_1.15-py3.6          2b73a275-7cbf-420b-a912-eae7f436e0bc  base
kernel-spark3.3-py3.9          2b7961e2-e3b1-5a8c-a491-482c8368839a  base
pytorch_1.2-py3.6              2c8ef57d-2687-4b7d-acce-01f94976dac1  base
spark-mllib_2.3                2e51f700-bca0-4b0d-88dc-5c6791338875  base
pytorch-onnx_1.1-py3.6-edt     32983cea-3f32-4400-8965-dde874a8d67e  base
spark-mllib_3.0-py37           36507ebe-8770-55ba-ab2a-eafe787600e9  base
spark-mllib_2.4                390d21f8-e58b-4fac-9c55-d7ceda621326  base
autoai-ts_rt22.2-py3.10        396b2e83-0953-5b86-9a55-7ce1628a406f  base
xgboost_0.82-py3.6             39e31acd-5f30-41dc-ae44-60233c80306e  base
pytorch-onnx_1.2-py3.6-edt     40589d0e-7019-4e28-8daa-fb03b6f4fe12  base
pytorch-onnx_rt22.2-py3.10     40e73f55-783a-5535-b3fa-0c8b94291431  base
default_r36py38                41c247d3-45f8-5a71-b065-8580229facf0  base
autoai-ts_rt22.1-py3.9         4269d26e-07ba-5d40-8f66-2d495b0c71f7  base
autoai-obm_3.0                 42b92e18-d9ab-567f-988a-4240ba1ed5f7  base
pmml-3.0_4.3                   493bcb95-16f1-5bc5-bee8-81b8af80e9c7  base
spark-mllib_2.4-r_3.6          49403dff-92e9-4c87-a3d7-a42d0021c095  base
xgboost_0.90-py3.6             4ff8d6c2-1343-4c18-85e1-689c965304d3  base
pytorch-onnx_1.1-py3.6         50f95b2a-bc16-43bb-bc94-b0bed208c60b  base
autoai-ts_3.9-py3.8            52c57136-80fa-572e-8728-a5e7cbb42cde  base
spark-mllib_2.4-scala_2.11     55a70f99-7320-4be5-9fb9-9edb5a443af5  base
spark-mllib_3.0                5c1b0ca2-4977-5c2e-9439-ffd44ea8ffe9  base
autoai-obm_2.0                 5c2e37fa-80b8-5e77-840f-d912469614ee  base
spss-modeler_18.1              5c3cad7e-507f-4b2a-a9a3-ab53a21dee8b  base
cuda-py3.8                     5d3232bf-c86b-5df4-a2cd-7bb870a1cd4e  base
autoai-kb_3.1-py3.7            632d4b22-10aa-5180-88f0-f52dfb6444d7  base
pytorch-onnx_1.7-py3.8         634d3cdc-b562-5bf9-a2d4-ea90a478456b  base
-----------------------------  ------------------------------------  ----
Note: Only first 50 records were displayed. To display more use 'limit' parameter.
software_space_uid = Client.software_specifications.get_uid_by_name('tensorflow_rt22.1-py3.9')
software_space_uid
'acd9c798-6974-5d2f-a657-ce06e986df4d'
model_details = Client.repository.store_model(model="/content/forest_fire_detection.tgz",meta_props={
    Client.repository.ModelMetaNames.NAME:"CNN Model for Forest fire detection",
    Client.repository.ModelMetaNames.TYPE:"tensorflow_2.7",
    Client.repository.ModelMetaNames.SOFTWARE_SPEC_UID:software_space_uid
})
model_details
{'entity': {'hybrid_pipeline_software_specs': [],
  'software_spec': {'id': 'acd9c798-6974-5d2f-a657-ce06e986df4d',
   'name': 'tensorflow_rt22.1-py3.9'},
  'type': 'tensorflow_2.7'},
 'metadata': {'created_at': '2022-11-11T21:05:25.592Z',
  'id': '5b00deac-d7d6-42fb-86d5-85db521f4895',
  'modified_at': '2022-11-11T21:05:27.865Z',
  'name': 'CNN Model for Forest fire detection',
  'owner': 'IBMid-66100457F5',
  'resource_key': '502f7e12-df84-4de4-bad4-187fca47b231',
  'space_id': '54f66e28-7d03-4808-8e64-b0c3b4826004'},
 'system': {'warnings': []}}
model_id = Client.repository.get_model_uid(model_details)
model_id
This method is deprecated, please use get_model_id()
/usr/local/lib/python3.7/dist-packages/ibm_watson_machine_learning/repository.py:1453: UserWarning: This method is deprecated, please use get_model_id()
  warn("This method is deprecated, please use get_model_id()")
'5b00deac-d7d6-42fb-86d5-85db521f4895'
#Downloading the model from IBM Cloud
Client.repository.download(model_id,'ffd_model.tgz')
Successfully saved model content to file: 'ffd_model.tgz'
'/content/ffd_model.tgz'