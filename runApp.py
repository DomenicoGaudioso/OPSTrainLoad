import streamlit as st

from stpyvista import stpyvista
from stpyvista.utils import is_the_app_embedded, start_xvfb
from streamlit_pdf_viewer import pdf_viewer
import  streamlit_toggle as tog
from streamlit_option_menu import option_menu

import graphviz
import pandas as pd
from io import StringIO
from SALib.analyze import sobol
import plotly.graph_objects as go
import os
from PIL import Image
import json

from functionOPS import *
from monitoring import *
from OTTfunction import *

#Initial configuration
#SBLOCCARE SOLO PER ONLINE
# start_xvfb()
# st.session_state.is_app_embedded = st.session_state.get(
#     "is_app_embedded", is_the_app_embedded()
# ) 


#from stpyvista.utils import start_xvfb
# from contextlib import contextmanager, redirect_stdout
# from io import StringIO
# from time import sleep
st.set_page_config(page_icon="🚄", page_title=":rainbow[𝒻𝑒𝓂 DTO]  ", layout="wide")


with st.sidebar:
   st.title(' 🚄 :rainbow[𝒻𝑒𝓂 DTO]  ') #💻🌈🖱️
   txtName2 = ":red[**F**]:gray[inite]  :orange[**E**]:gray[lement] :green[**M**]:gray[odel]  :gray[_for_] :green[**D**]:gray[igital]  :blue[**T**]:gray[win]  :gray[_with_] :violet[**O**]:gray[penSees]"
               
   st.markdown(txtName2)
   imageName = 'LogoDTWIN-Modello-removebg-preview.png'
   isertImage(imageName, width = 210)


   # Utilizza st.markdown per inserire i link
   st.markdown("## Contacts")
   st.write("Name: Domenico")
   st.write("Surname: Gaudioso")
   st.write("📧 dome.gaudioso@gmail.com")
   st.markdown("📱 [LinkedIn]({'https://www.linkedin.com/in/il_tuo_profilo_linkedin'})", unsafe_allow_html=True)
   st.markdown("💻 [GitHub]({'https://github.com/DomenicoGaudioso'})", unsafe_allow_html=True)

   st.markdown("## About")
   # Link di Streamlit
   st.markdown(f"[Streamlit]({'https://www.streamlit.io/'})", unsafe_allow_html=True)
   # Link di SciPy
   st.markdown(f"[SciPy]({'https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.differential_evolution.html'})", unsafe_allow_html=True)
   # Link di Sobol Sequences (sobol_seq su PyPI)
   st.markdown(f"[SALib]({'https://salib.readthedocs.io/en/latest/'})", unsafe_allow_html=True)


txtName2 = " **🚄 :rainbow[𝒻𝑒𝓂 DTO]**  -- :red[**F**]:gray[inite]  :orange[**E**]:gray[lement] :green[**M**]:gray[odel]  :gray[_for_] :green[**D**]:gray[igital]  :blue[**T**]:gray[win]  :gray[_with_] :violet[**O**]:gray[penSees]"
            
st.markdown(txtName2)
selected3 = option_menu(None, ["Info", "Upload", "SetPar", "Sensy", 'Optm', "Damg",
                               "MovingLA", "WNoise", "Quake", "Other"],
                         
    icons=['book-half', 'cloud-arrow-up-fill', "bar-chart-steps", "eyedropper", "cpu-fill","bandaid-fill", "truck", "magic", "broadcast", "clipboard2-pulse-fill"], 
    menu_icon="cast", default_index=0, orientation="horizontal"
)

if selected3 == "Info":
   # Descrizione
   st.markdown("""
   This tool is designed to calibrate Finite Element Method (FEM) models through modal analysis, combining scientific precision with powerful optimization and digital twin capabilities.
   ### How It Works:
   Grafico per l'utilizzo
   """)

   # Create a graphlib graph object
   graph = graphviz.Digraph()
   graph2 = graphviz.Digraph() 
   graph3 = graphviz.Digraph() 
   graph.attr('node', shape='doublebox')
   
   with graph.subgraph(name='cluster_start') as c:
      c.attr(color='blue')
      c.node_attr['style'] = 'filled'
      c.node('Model')
      c.attr(label='START')

   graph.attr('node', shape='doublebox')
   graph.node('Set optmization parameter')
   
   graph.edge('Model', 'Set optmization parameter')
   graph.edge('Model', 'model analysis', label='preliminary Analysis')
   
   with graph2.subgraph(name='cluster_end') as c:
      c.attr(color='blue')
      c.node_attr['style'] = 'filled'
      c.node('static Analisys')
      c.node('modal Analisys')
      c.node('bucking Analisys')
      c.node('moving load Analisys')
      c.node('white noise Analisys')
      c.node('quake Analisys')
      c.attr(label='Structural Analysis of Model Analysis')

   with graph3.subgraph(name='cluster_mid') as c:
      c.attr(color='blue')
      c.node_attr['style'] = 'filled'
      c.node('frequency')
      c.node('frequency and shape model')
      c.node('deformad with static analysis')
      c.attr(label='Sensitivity and Optmization Analysis')
      
   #graph.edge('model analysis', 'static Analisys')
   #graph.edge('model analysis', 'modal Analisys')
   #graph.edge('model analysis', 'bucking Analisys')
   #graph.edge('model analysis', 'moving load Analisys')
   #graph.edge('model analysis', 'white noise Analisys')
   #graph.edge('model analysis', 'quake Analisys')
    
   graph.edge('Set optmization parameter', 'sensitivity analysis')
   #graph.edge('sensitivity analysis', 'frequency')
   #graph.edge('sensitivity analysis', 'frequency and shape model')
   #graph.edge('sensitivity analysis', 'deformad with static analysis')
   
   graph.edge('sensitivity analysis', 'Set optmization parameter')
   graph.edge('Set optmization parameter', 'optimization analysis')
   #graph.edge('optimization analysis', 'frequency')
   #graph.edge('optimization analysis', 'frequency and shape model')
   #graph.edge('optimization analysis', 'deformad with static analysis')
   graph.edge('optimization analysis', 'model calibrated (Digital Twin)')
   
   #graph.edge('frequency', 'model calibrated (Digital Twin)')
   #graph.edge('frequency and shape model', 'model calibrated (Digital Twin)')
   #graph.edge('deformad with static analysis', 'model calibrated (Digital Twin)')

   graph.edge('model calibrated (Digital Twin)', 'model analysis', label='last Analysis')

   
   st.graphviz_chart(graph)
   st.graphviz_chart(graph2)
   st.graphviz_chart(graph3)
   
   imageName = 'DALL·E 2023-11-16 12.43.27 - quadro che rappresenta un ponte bello.png'
   inputPDF = "documentazioneFEMDTO.pdf"
   pdf_viewer(inputPDF, height=1300, width= 1200)

   #isertImage(imageName, width = 1350)



## IMPORT JSON FILE
if selected3 == "Upload":
   Modelfile = st.file_uploader("excel file of model fem", key="excelModel", type=["xlsx"])
   #st.write(" Import the file after Save file with this command in openseespy: ops.printModel('JSON', -file', 'filename') and ops.printModel(-file', 'filename')")

   #ModelfileTXT = st.file_uploader("Choose txt file Model", key="TxtModel")
   #st.write(" Import the file after Save file with this command in openseespy: ")

   if Modelfile is not None:
      
         # Leggi tutti i fogli del file Excel
         xls = pd.ExcelFile(Modelfile)

         dictOPS = xlsxtoJSON(xls)
         st.session_state['Model'] = dictOPS

   try:
      st.markdown('View **dictionary Model**.')
      st.json(st.session_state.Model, expanded=False)

      #JSONtoOPS(dictOPS) #create model in openseespy

      #plot model
      st.markdown('View **Model 3D**.')
      cols1, cols2, cols3, cols4 = st.columns([1,1,1,1])
      with cols1:
         toggle1 = st.toggle(label='Activate view', 
                     key="KeyToogle1", 
                     value=True, 
                     )
      with cols2:
         toggle2 = st.toggle(label='Node', 
                     key="KeyToogle2", 
                     value=True, 
                     )
      with cols3:
         toggle3 = st.toggle(label='Label Node', 
                     key="KeyToogle3", 
                     value=False, 
                     )
      with cols4:
         toggle4 = st.toggle(label='Label Element', 
                     key="KeyToogle4", 
                     value=False, 
                     )
         
      st.markdown('**Scale View**')
      cols1, cols2, cols3, cols4 = st.columns([1,1,1,1])
      with cols1:
         toggle5 = st.number_input("node", value=1.00, step = 0.01, key= "scaleNode")
      with cols2:
         toggle6 = st.number_input("beam", value=1.00, step = 0.01, key= "scaleBeam")
      with cols3:
         toggle7 = st.number_input("link", value=1.00, step = 0.01, key= "scaleLink")
      with cols4:
         toggle8 = st.number_input("support", value=1.00, step = 0.01, key= "scaleSupport")

      st.markdown('**Color View**')
      cols1, cols2, cols3, cols4, cols5, cols6, cols7 = st.columns([1,1,1,1, 1, 1, 1])
      with cols1:
         color1 = st.color_picker("background", "#ffffff","colorbackground")
      with cols2:
         color2 = st.color_picker("node", "#ff00ff","colorNode")
      with cols3:
         color3 = st.color_picker("beam", "#0000ff","colorBeam")
      with cols4:
         color4 = st.color_picker("shell", "#00ffff","colorShell")
      with cols5:
         color5 = st.color_picker("brick", "#ff00ff","colorBrick")
      with cols6:
         color6 = st.color_picker("rigidLink", "#ffff00","colorRigidLink")
      with cols7:
         color7 =  st.color_picker("twoNodeLink", "#ffA500","colorTwoNodeLink")
         
      scale = {"node": toggle5, "beam": toggle6, "link": toggle7, "support": toggle8}
      colorDict = {"background": color1, "node": color2, "beam": color3, "shell": color4, "brick": color5, "rigidLink": color6,  "twoNodeLink": color7}
      
      if toggle1:
         plotModel = opsModelPlot3d(st.session_state.Model, nodeView=toggle2, nodeLabel = toggle3, scaleS=scale, color = colorDict)
         stpyvista(plotModel, panel_kwargs=dict(orientation_widget=True))  #key="pvPlotModel"

   except:
      st.warning('The files to create the model have not been inserted or are incorrect' , icon="⚠️")



dictCalibr = persistdata()


if selected3 == "SetPar":

   ## IMPORT JSON FILE FOR DEFINE PARAMETER OPTMIZETION
   dictJSON = st.file_uploader("JSON Params", key="JsonParams")
   
   if dictJSON is not None:

      # Read file :
      dictImport = json.loads(StringIO(dictJSON.getvalue().decode("utf-8")).read())
      dictCalibr = persistdata(dictImport)
      st.session_state['dictParams'] = dictCalibr
      #dictCalibr = json.loads(dictJSON)
   

   try:
      nodeTag, matTag, secTag, beamTag, shellTag, brickTag = listTag(st.session_state.Model)
   except:
      nodeTag, matTag, secTag, beamTag, shellTag, brickTag = [], [], [], [], [], []
      
   st.session_state["nodeTag"] = nodeTag

   ## DEFINE TITLE
   with st.container():
      col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])
      with col1:
         st.markdown(" ")

      with col2:   
         st.markdown("TAG")
      with col3:
         st.markdown("PARAMETER")
      with col4:
         st.markdown("VALUE MIN")
      with col5:
         st.markdown("VALUE MAX")
      with col6:
         st.markdown("ASSIGN")

   #MATERIAL
   with st.container():
      col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])
      with col1:
         st.markdown("Material parameter 🧱")

      with col2:
         optionTag = st.multiselect(
         "tag",
         matTag, key= "matTag", label_visibility = "collapsed"
      )   
      with col3:
         optionParams = st.selectbox(
         "parameter",
         ('E', 'G', 'v', 'rho'), key= "matParams", label_visibility= "collapsed"
      )
      with col4:
         optionValMin = st.number_input("value Min", value=1, min_value = 1, step = 1, key= "matValMin", label_visibility = "collapsed")
         
      with col5:
         optionValMax = st.number_input("value Max", value=1, min_value = 1, step = 1, key= "matValMax", label_visibility = "collapsed") 
      
      with col6:
         # Creare uno spazio vuoto per allineare il pulsante con la sidebar
         buttonAss = st.button("\nAssign\n", type="primary", key="ButtonMatParams")
   
      if buttonAss:
         dictCalibr["material"].append({"tag": optionTag, 
                                        "parameter": optionParams, 
                                        "value_min": optionValMin, 
                                        "value_max": optionValMax})

   ## DEFINE SECTION OPTIMIZATION
   with st.container():
      col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])
      with col1:
         st.markdown("Section parameter 🔲")

      with col2:
         optionTag = st.multiselect(
         "tag",
         secTag, key= "secTag", label_visibility= "collapsed"
      )   
      with col3:
         optionParams = st.selectbox(
         "parameter",
         ('E', 'G', 'A', 'Iz', 'Iy', 'Jxx'), key= "secParams", label_visibility= "collapsed"
      )
      with col4:
         optionValMin = st.number_input("value Min", value=1, min_value = 1, step = 1, key= "secValMin", label_visibility= "collapsed")
         
      with col5:
         optionValMax = st.number_input("value Max", value=1, min_value = 1, step = 1, key= "secValMax", label_visibility= "collapsed")   
         
      with col6:
         buttonAss = st.button("Assign", type="primary", key="ButtonSecParams")
      
      if buttonAss:
         dictCalibr["section"].append({"tag": optionTag, 
                                        "parameter": optionParams, 
                                        "value_min": optionValMin, 
                                        "value_max": optionValMax})
  
   ## DEFINE ELEMENT OPTIMIZATION 
   with st.container():
      col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])
      with col1:
         st.markdown("Element parameter 🦾")

      with col2:
         optionTag = st.multiselect(
         "tag",
         beamTag, key= "eleTag", label_visibility= "collapsed"
      )   
      with col3:
         optionParams = st.selectbox(
         "parameter",
         ('E', 'G', 'A', 'Iz', 'Iy', 'Jxx'), key= "eleParams", label_visibility= "collapsed"
      )
      with col4:
         optionValMin = st.number_input("value Min", value=1, min_value = 1, step = 1, key= "eleValMin", label_visibility= "collapsed")
         
      with col5:
         optionValMax = st.number_input("value Max", value=1, min_value = 1, step = 1, key= "eleValMax", label_visibility= "collapsed") 
         
      with col6:
         buttonAss = st.button("Assign", type="primary", key="ButtonEleParams")
      
      if buttonAss:
         dictCalibr["beamEle"].append({"tag": optionTag, 
                                        "parameter": optionParams, 
                                        "value_min": optionValMin, 
                                        "value_max": optionValMax})
           
   ## DEFINE LOAD NODE OPTIMIZATION
   
   with st.container():
      col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])
      with col1:
         st.markdown("Load Node parameter 🟠")
      with col2:
         optionTag = st.multiselect(
         "tag node",
         nodeTag, key= "nodeTagLoad", label_visibility= "collapsed"
      )   
      with col3:
         optionParams = st.selectbox(
         "parameter",
         ('Px', 'Py', 'Pz', 'Mx', 'My', 'Mz', 'Mass'), key= "nodeLoadParams", label_visibility= "collapsed"
      )
      with col4:
         optionValMin = st.number_input("value Min", value=1, min_value = 1, step = 1, key= "nodeEleValMin", label_visibility= "collapsed")
         
      with col5:
         optionValMax = st.number_input("value Max", value=1, min_value = 1, step = 1, key= "nodeEleValMax", label_visibility= "collapsed") 
         
      with col6:
         buttonAss = st.button("Assign", type="primary", key="ButtonNodeLoadParams")
      
      if buttonAss:
         dictCalibr["nodeLoad"].append({"tag": optionTag, 
                                        "parameter": optionParams, 
                                        "value_min": optionValMin, 
                                        "value_max": optionValMax})

   ## DEFINE LOAD ELEMENT OPTIMIZATION
   with st.container():
      col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])
      with col1:
         st.markdown("Load Element parameter 🟦")

      with col2:   
         optionTag = st.multiselect(
         "tag ele",
         beamTag, key= "eleTagLoad", label_visibility= "collapsed"
      )   
      with col3:
         optionParams = st.selectbox(
         "parameter",
         ('px', 'py', 'pz', 'mx', 'my', 'mz'), key= "eleLoadParams", label_visibility= "collapsed"
      )
      with col4:
         optionValMin = st.number_input("value Min", value=1, min_value = 1, step = 1, key= "loadEleValMin", label_visibility= "collapsed")
         
      with col5:
         optionValMax = st.number_input("value Max", value=1, min_value = 1, step = 1, key= "loadEleValMax", label_visibility= "collapsed") 
         
      with col6:
         buttonAss = st.button("Assign", type="primary", key="ButtonEleLoadParams")

      if buttonAss:
         dictCalibr["beamLoad"].append({"tag": optionTag, 
                                        "parameter": optionParams, 
                                        "value_min": optionValMin, 
                                        "value_max": optionValMax})

   if st.button("Reset", type="primary", key="resetDictionary"):
      st.cache_resource.clear()
      dictCalibr = {"material": [],
               "section": [],
               "beamEle": [],
               "nodeLoad": [],
               "beamLoad": [],
               }
      
   st.session_state['dictParams'] = dictCalibr
   st.markdown("List of parameter set")         
   st.write(dictCalibr)
   
   
   st.markdown("Inserire un file dictionari per la definizione dei carichi, load pattern, tipo di carichi ed elementi/nodi a cui applicare il carico")
   # Caricamento del file Excel tramite widget di Streamlit
   file = st.file_uploader("Carica un file Excel", type=["xlsx", "xls"])

   if file is not None:
      # Leggi il file Excel usando Pandas
      excel_data = pd.read_excel(file, sheet_name=None)
      st.session_state["Load"] = excel_data

   # Mostra i dati del foglio di lavoro selezionato come DataFrame
   try:
      # Mostra i nomi dei fogli di lavoro nel file Excel
      sheet_names = list(st.session_state.Load.keys())
      selected_sheet = st.selectbox("Visualizza un foglio di lavoro", sheet_names)
      if selected_sheet:
         st.write(f"Contenuto del foglio di lavoro '{selected_sheet}':")
         st.write(st.session_state.Load[selected_sheet])
   except:
      pass
   


## DEFINE SENSITIVITY ANALISYS
if selected3 == "Sensy":
   pathfolder = "output_Sensitivity"
   os.makedirs(pathfolder, exist_ok=True)
   
   st.markdown("View Dictionary of parameters to study")
   st.json(st.session_state.dictParams, expanded=False)
   
   st.markdown("set parameter befor run Analysis")
   Col1, Col2, Col3, Col4 = st.columns([1, 1, 1, 1])
   with Col1:
      samples = st.number_input("samples", value = 10, key ="sampleSensityviti")
   with Col2:
      numModes = st.number_input("number of Modes", value = 10, key ="modalModesSampleSensityviti")
      
   with Col3: 
      try:
         lpList = st.session_state["Load"]["LoadPattern"]["Name"].tolist()
         lpList.append("All")
         optionLP = st.selectbox("load Pattern to Run", lpList, key="lpSensRun")
      except:
         optionLP = st.selectbox("load Pattern to Run", "⚠️", key="lpSensRun")
      
   with st.expander("Frequency Sensitivity Analisys"):
      st.markdown("The FEM model is study by modal analysis")
      st.markdown("Click the button below to launch the optimizer and 🙏")
      
      if st.button('Run frequency sensitivity analisys'):
         JSONtoOPS(st.session_state.Model) #create model in openseespy
         modalSens = ModalSensitivity(st.session_state.Model, st.session_state.dictParams, samples, numModes)
         st.session_state["modalSens"] = modalSens
         ops.wipe()
      
         
   #if st.session_state.modalSens is not None:
   try:
      sensView = st.slider('view frequency Sobol index', 0, numModes, key="sensView")
      listKey = list(st.session_state.modalSens.keys())[sensView]
      total_Si, first_Si, second_Si = st.session_state.modalSens[listKey].to_df()
      
      st.markdown("Total Si")
      st.dataframe(total_Si)
      st.markdown("First Si")
      st.dataframe(first_Si)
      st.markdown("Second Si")
      st.dataframe(second_Si)
   except:
      st.warning('for view result you have define model, parameter of sensitivity analisys and click **Run**' , icon="⚠️")
      

         
      # axes = modalSens[listKey].plot()
      # axes[0].set_yscale('log')
      # fig = plt.gcf()  # get current figure
      # fig.set_size_inches(10, 4)
      # plt.tight_layout()
      # plt.show()

      #SALib.plotting.heatmap.heatmap(modalSens[listKey].to_df(), metric: str, index: str, title: str = None, ax=None)[source]



      #modalSens[listKey].heatmap()


# Note that if the sample was created with `calc_second_order=False`
# Then the second order sensitivities will not be returned
# total_Si, first_Si = Si.to_df()


## DEFINE CALIBRATION
if selected3 == "Optm":
   pathfolder = "output_Optmization"
   os.makedirs(pathfolder, exist_ok=True)
   
   os.makedirs(os.path.join(pathfolder, 'ott_frequency'), exist_ok=True)
   os.makedirs(os.path.join(pathfolder, 'ott_OMA'), exist_ok=True)
   os.makedirs(os.path.join(pathfolder, 'ott_Static'), exist_ok=True)
   os.makedirs(os.path.join(pathfolder, 'ott_Static_OMA'), exist_ok=True)
   
   
   try:
      st.markdown("View Dictionary of parameters to optimize")
      st.json(st.session_state.dictParams, expanded=False)
   except:
      st.warning('**WARNING** set params of optmization in **OPTM** page' , icon="⚠️")
   
   st.markdown("Set parameter params.")
   
   optCol1, optCol2, optCol3, optCol4, optCol5, optCol6 = st.columns([1, 1, 1, 1, 1, 1])
   
   with optCol1:
      ott_nM = st.number_input("numero modi", 12, help="numero di modi nell'analisi Modale", key="ott_nM")
      
   with optCol2:
      ott_fMin = st.number_input("frequenza minima", 0.0, help="le frequenze minori di questo parametro verranno scartate", key="ott_fMin")
      
   with optCol3: 
      try:
         lpList = st.session_state["Load"]["LoadPattern"]["Name"].tolist()
         lpList.append("All")
         optionLP = st.multiselect("load Pattern to Run", lpList, key="lpOttRun")
      except:
         optionLP = st.selectbox("load Pattern to Run", "⚠️", key="lpOttRun")
         
   with optCol4:
      try:
         dictFLoad = []
         for i in optionLP:
            dictFLoad.append({"LP": i, "scale": 1})
            
         dfOtt_LP = pd.DataFrame(dictFLoad)
         edited_df = st.data_editor(dfOtt_LP)
         ott_scaleLP = dfOtt_LP.loc[:, 'scale'].tolist() #st.text_input("scale Load Pattern", "1.0", help="scalere il carico da assegnare come massa", key="ott_scaleLP")
      except:
         ott_scaleLP = st.selectbox("definire i carichi", "⚠️", key="ott_scaleLP")
         
         
   with optCol5:
      option = st.selectbox(
   'strategy',
   ("best1bin","best1exp", "rand1exp","randtobest1exp",
      "currenttobest1exp","best2exp","rand2exp","randtobest1bin",
      "currenttobest1bin","best2bin","rand2bin","rand1bin"))
      
   with optCol6:
      option = st.selectbox(
   'init',
   ("latinhypercube","sobol","halton","random"))
      
   
   
   freqRef_files = st.file_uploader("frequency csv file for **frequency optimization**", accept_multiple_files=False)
   if freqRef_files is not None:
      bytes_data = freqRef_files.read()
      # To convert to a string based IO:
      stringio = StringIO(freqRef_files.getvalue().decode("utf-8"))
      # To read file as string:
      string_data = stringio.read()
      expFreq_Dict = readFrequencyCorr(string_data) #trasform in dictionary
      st.markdown("View Dictionary of frequency target and weight")
      st.write(expFreq_Dict)
      
   corr_files = st.file_uploader("correspondence csv file for **OMA optimization**", accept_multiple_files=False, type="csv")
   omaRef_files = st.file_uploader("oma excel file for **OMA optimization**", accept_multiple_files=False, type="xlsx")
   staticRef_files = st.file_uploader("static excel file for **Static optimization**", accept_multiple_files=False, type="xlsx")
   
   try:
      n_modiOma = list(pd.read_excel(omaRef_files, index_col=0))
      dictAB = []
      for i in n_modiOma:
         dictAB.append({"Mode": i, "αi": 1, "βi": 1})
         
      dfOtt_LP = pd.DataFrame(dictAB)
      paramsAB = st.data_editor(dfOtt_LP)
      #ott_scaleLP = dfOtt_LP.loc[:, 'scale'].tolist() #st.text_input("scale Load Pattern", "1.0", help="scalere il carico da assegnare come massa", key="ott_scaleLP")
   except:
      st.warning('**WARNING** load oma excel file' , icon="⚠️")

   plusInput = (ott_nM, ott_fMin, optionLP, ott_scaleLP) 
   
         
   nameXaxis = 'number of iteration'
   nameYaxis = "valor of funcion optimizer "
      
   with st.expander("Frequency optimization"):
      st.markdown("The FEM model is currently being calibrated through modal analysis, comparing the obtained frequencies with the target values.")
      st.markdown("The optimization function is as follows:")
      st.latex(r'''
         E = 
         \sum_{i=1}^{n} \alpha_i
         \left(\frac{f_{FEM}-f_{exp}}{f_{FEM}}\right)^{2}
         ''')
         
         
      st.markdown("Click the button below to launch the optimizer and 🙏")
      if st.button('Run frequency optimize'):
         if freqRef_files is not None:
            #JSONtoOPS(st.session_state.Model) #create model in openseespy
            optmization1 = Optimization(dictFrequency = expFreq_Dict, excelLoad=st.session_state["Load"])     
            st.session_state["result_ott1"] = optmization1.RunOptimizer(st.session_state.Model, st.session_state.dictParams, plusInput)
            #RunOptimizer(st.session_state.Model, st.session_state.dictParams)
            #Mplus = Mplus, recorder = True, printOut = False, reportFileName = False
            fM = OPS_Modal(ott_nM)
            st.write(fM)
            ops.wipe()
            make_chart(optmization1.Niteration, optmization1.storyOptimum, nameXaxis, nameYaxis)
            st.write(st.session_state.result_ott1)


         else:
            st.warning('Warning, insert frequency referens file (.cvs)', icon="⚠️")
         
      
   with st.expander("OMA optimization"):
      st.markdown("The FEM model is currently being calibrated through modal analysis, comparing the obtained frequencies with the target values as indicated in the OMA file, which includes the frequencies and modal shapes. The optimization function is as follows:")
      st.latex(r'''
         E = 
         \sum_{i=1}^{n} \alpha_i
         \left(\frac{f_{FEM}-f_{exp}}{f_{FEM}}\right)^{2} 
         +
         \sum_{j=1}^{n} \beta_i
         \left({1-MAC_{[j,j]}}\right)
         ''')
      

      if corr_files is not None:
         df_corr = pd.read_csv(corr_files, sep= ";", index_col=0, usecols=['sensorID', 'femID'])
         #st.write(df_corr.to_dict())

      if omaRef_files is not None:
         df_oma = pd.read_excel(omaRef_files, index_col=0)
         #st.write(df)

      st.session_state["result_ott2"] = None
      st.markdown("Click the button below to launch the optimizer and 🙏")
      
      
      if st.button('Run OMA optimize'):
         if omaRef_files is not None and corr_files is not None:
            #JSONtoOPS(st.session_state.Model) #create model in openseespy
            optmization2 = Optimization(dictOMAfile = df_oma, dictCorr = df_corr, excelLoad=st.session_state["Load"], par_ab = paramsAB, typeOptimum= 2)
            st.session_state["result_ott2"] = optmization2.RunOptimizer(st.session_state.Model, st.session_state.dictParams, plusInput)
            #ops.wipe()
            st.markdown("View Dictionary of parameters included in the parametric analysis.")
            make_chart(optmization2.Niteration2, optmization2.storyOptimum2, nameXaxis, nameYaxis)
            st.write(st.session_state.result_ott2)
         else:
            st.warning('Warning, insert OMA referens file (.cvs) and\or correspondence node', icon="⚠️")
            
      
      if st.session_state.result_ott2 is not None:
         #if omaRef_files is not None and corr_files is not None:
            #on = st.toggle('view result fem vs result oma')
         #if on:
         #JSONtoOPS(st.session_state.Model) #create model in openseespy
         OMA_dict, dictEV_fem, omaPos = dataframe_OMA(df_corr, df_oma, nM = ott_nM, fmin = ott_fMin, pathSave = None)
         #fissare pathSave per far salvare i risultati della modale
         

         #plot MaC
         plotMAC(OMA_dict, dictEV_fem)
         
         #figPlotOma = plotOMA_confronto(df_corr, df_oma, nM = ott_nM, fmin = ott_fMin)
         #st.plotly_chart(figPlotOma[omaFigView], theme="streamlit", use_container_width=True)
         st.session_state["figPlotOma"] = plotOMA_confronto(df_corr, OMA_dict, dictEV_fem, omaPos)


         tablist = st.tabs(["EV" + str(iNM) for iNM in range(1, len(st.session_state.figPlotOma)) ])
         for inT in range(0, len(tablist)):  
            with tablist[inT]:
               st.plotly_chart(st.session_state.figPlotOma[inT], theme="streamlit", use_container_width=True) 

            
   with st.expander("Static optimization WIP"):
      st.markdown("The FEM model is currently being calibrated through static analysis, comparing the obtained displacement with the target values as indicated in the displacement file, which includes the and displacement shapes. The optimization function is as follows:")
      st.latex(r'''
         E = 
         \sum_{i=1}^{n} \alpha_i
         \left(\frac{\delta_{FEM}-\delta_{exp}}{\delta_{FEM}}\right)^{2}
         ''')
      
      st.markdown("Click the button below to launch the optimizer and 🙏")
      if st.button('Run static optimize'):
         st.warning('⚠️ **W.I.P.** ' , icon="⚠️") 
         
   with st.expander("Static and OMA optimization **WIP**"):
      st.markdown("optmization with two function goal")
      st.latex(r'''
         E_1 = 
         \sum_{i=1}^{n} \alpha_i
         \left(\frac{\delta_{FEM}-\delta_{exp}}{\delta_{FEM}}\right)^{2}
         ''')
      
      st.latex(r'''
         E_2 = 
         \sum_{i=1}^{n} \alpha_i
         \left(\frac{f_{FEM}-f_{exp}}{f_{FEM}}\right)^{2} 
         +
         \sum_{j=1}^{n} \beta_i
         \left({1-MAC_{[j,j]}}\right)
         ''')
      
      st.markdown("Click the button below to launch the optimizer and 🙏")
      if st.button('Run static and OMA optimize'):
         st.warning('⚠️ **W.I.P.** ' , icon="⚠️") 

## DAMAGE
if selected3 == "Damg":
   st.markdown("View Dictionary of parameters to optimize")
   try:
      st.json(st.session_state.dictParams, expanded=False)
   
      st.markdown("Set node save result")
      nodeSave = st.multiselect("nodeTag", st.session_state.nodeTag, key= "nodeTagDamage", label_visibility = "collapsed") 
   except:
      st.warning('Non sono stati settati i parametri di ottimizzazione' , icon="⚠️")

   with st.expander("Damage with remove element"):
      
      if st.button("Run", key= "Damage1"):
         with st.spinner("Please wait ..."):
            listResultDamage1 = RunDamageRemove(st.session_state.Model, st.session_state.dictParams, nodeSave = nodeSave, nM = 12)
         st.success('Done!')
         indexName = ["S"+str(i+1) for i in range(0, len(listResultDamage1)-1)]
         indexName.insert(0, "SND") #scenario di assenza di degrado
         print(len(indexName), len(listResultDamage1))
         dfD1 = pd.DataFrame(listResultDamage1, index=indexName)
         

         # Converte le liste in array NumPy
         #df_np_arrays = dfD1.applymap(np.array)

         # Estrai la lista corrispondente alla riga "SND"
         snd_row = dfD1.loc["SND"]

         # Crea un nuovo DataFrame per le differenze percentuali
         df_percent_diff = pd.DataFrame(index=dfD1.index, columns=dfD1.columns)

         # Itera su tutte le colonne e righe del DataFrame
         for col in dfD1.columns:
            for row in dfD1.index:

               # Sottrai un numero da ciascun elemento nella lista
               diff = [item - dfD1.at[row, col][idx] for idx, item in enumerate(snd_row[col])]

               # Calcola la differenza percentuale in valore assoluto
               df_percent_diff.at[row, col] = [abs((item / dfD1.at[row, col][idx]) - 1) * 100 for idx, item in enumerate(diff)]

         
         st.session_state["df_damage1_percentuali"] = df_percent_diff
         st.session_state["df_damage1"] = dfD1
         # Funzione per estrarre il primo elemento dalla lista
         # Funzione per estrarre un elemento specifico dalla lista


      # Indice specificato esternamente
      nM = 7
      values = st.slider('Select modes',1, nM, 1)
      # Applica la funzione a ciascuna cella del DataFrame con l'indice specificato
      try:
         df_estratto = st.session_state.df_damage1_percentuali.applymap(lambda x: estrai_elemento(x, values))


         # Applica la funzione a ciascuna cella del DataFrame
         st.markdown("## Result")
         st.dataframe(st.session_state.df_damage1.applymap(lambda x: estrai_elemento(x, values)))
         st.markdown("## Differenza")
         st.dataframe(df_estratto.style.background_gradient(vmin=0.0, vmax=100.0, cmap='RdYlGn'))
      except:
         pass


   with st.expander("Damage with degrade element"):
      

      if st.button("Run", key= "Damage2"):
         with st.spinner("Please wait ..."):
            listResultDamage2, listName = RunDamageDegrade(st.session_state.Model, st.session_state.dictParams, nodeSave = nodeSave, nM = 12)
         st.success('Done!')
         indexName = listName
         indexName.insert(0, "SND") #scenario di assenza di degrado
         print(len(indexName), len(listResultDamage2))
         dfD2 = pd.DataFrame(listResultDamage2, index=indexName)
         

         # Converte le liste in array NumPy
         #df_np_arrays = dfD1.applymap(np.array)

         # Estrai la lista corrispondente alla riga "SND"
         snd_row = dfD2.loc["SND"]

         # Crea un nuovo DataFrame per le differenze percentuali
         df2_percent_diff = pd.DataFrame(index=dfD2.index, columns=dfD2.columns)

         # Itera su tutte le colonne e righe del DataFrame
         for col in dfD2.columns:
            for row in dfD2.index:

               # Sottrai un numero da ciascun elemento nella lista
               diff = [item - dfD2.at[row, col][idx] for idx, item in enumerate(snd_row[col])]

               # Calcola la differenza percentuale in valore assoluto
               df2_percent_diff.at[row, col] = [abs((item / dfD2.at[row, col][idx]) - 1) * 100 for idx, item in enumerate(diff)]

         
         st.session_state["df_damage2_percentuali"] = df2_percent_diff
         st.session_state["df_damage2"] = dfD2
         # Funzione per estrarre il primo elemento dalla lista
         # Funzione per estrarre un elemento specifico dalla lista


      # Indice specificato esternamente
      nM = 7
      values = st.slider('Select modes',1, nM, 1, key="sliderDamage2")
      # Applica la funzione a ciascuna cella del DataFrame con l'indice specificato
      try:
         df_estratto = st.session_state.df_damage2_percentuali.applymap(lambda x: estrai_elemento(x, values))


         # Applica la funzione a ciascuna cella del DataFrame
         st.markdown("## Result")
         st.dataframe(st.session_state.df_damage2.applymap(lambda x: estrai_elemento(x, values)))
         st.markdown("## Differenza")
         st.dataframe(df_estratto.style.background_gradient(vmin=0.0, vmax=100.0, cmap='RdYlGn'))
      
      except:
         pass
      
      # Visualizza il risultato
      #else:
      #st.dataframe(df_percent_diff)

## MOVING LOAD
if selected3 == "MovingLA":
   
   tagR11 = [204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289]
   tagR12 = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146]
   
   st.markdown("##### Rails Element")
   rail_1 = st.text_input('rail_1', 
                          tagR11, key = 'rail_1')
   rail_2 = st.text_input('rail_2', tagR12, key = 'rail_2')

   st.markdown("##### Train Load")
   dictTrain = json.load(open("TrainParams.json"))
   #dictCalibr = persistdata(dictTrain )
   st.session_state['dictTrain'] = dictTrain 
   #dictCalibr = json.loads(dictJSON)
   
   keyTrain = list(dictTrain.keys())
   typeTrain = st.selectbox(
   "Train for analisys",
   keyTrain,
   index=3,
   placeholder="Choose one Train",
   key= "trainType"
   )
   
   st.markdown("##### Speed")
   with st.container():
      col1, col2, col3 = st.columns([1, 1, 1])
      with col1:   
         vel_start = st.number_input('v_start [Km/h]', value=100, key="vel_start")
      with col2:  
         vel_end = st.number_input('v_end [Km/h]', value=100, key="vel_end")
      with col3:  
         vel_step = st.number_input('step', value=10, key="vel_step")
   
   st.markdown("##### Rayleigh damping")
   with st.container():
      col1, col2 = st.columns([1, 1])
      with col1:
         mode1_ref = st.number_input('Mode 1', value=0, key="mode1_ref")
         mode2_ref = st.number_input('Mode 1', value=1, key="mode2_ref")
      with col2:
         dampingHelp = "steel bridge: 0.24-0.5; Prestressed concreate: 0.32-1.0; Reinforced concrerate bridge: 0.32-1.5"
         zita_1 = st.number_input('ζ1 [%]', value=0.4, key="zita1", help=dampingHelp)
         zita_2 = st.number_input('ζ2 [%]', value=0.2, key="zita2")
   
   # Run
   rail_1 = [int(tag) for tag in rail_1.strip('][').split(', ')]
   rail_2 = [int(tag) for tag in rail_2.strip('][').split(', ')]
   
   # Recorder
   st.markdown("##### Recorder Output")
   with st.container():
      col1, col2 = st.columns([1, 1])
      with col1:
         nodeRecorder = st.checkbox('Node Recorder', key = 'Node Recorder', help =" se vuoi salvare output nodali")
         nodeRecorder_tag = st.text_input('Node Recorder tag', [  7,   15,    10,  238,  240,   242], key = 'NodeRecorder_tag')
      with col2:
         eleRecorder = st.checkbox('Ele Recorder (W.I.P.)', key = 'Ele Recorder ', help =" se vuoi salvare output degli elementi")
         eleRecorder_tag = st.text_input('Ele Recorder tag (W.I.P.)', [  7,   15,    10,  238,  240,   242], key = 'EleRecorder_tag')
   
   nodeOutput = [int(tag) for tag in nodeRecorder_tag.strip('][').split(', ')]
   eleOutput = [int(tag) for tag in eleRecorder_tag.strip('][').split(', ')]
         
   # Input Analisys
   st.markdown("##### Analisys input")
   with st.container():
      col1, col2 = st.columns([1, 1])
      with col1:
         secondFV = st.number_input('secondi', value=20, key="sFV", help = "durata oscillazioni libere (deltaT = 0.01)")
   
   if vel_start != vel_end:
      vel_list = list(range(vel_start, vel_end, vel_step))
   else:
      vel_list = [vel_start]
      
   
   if st.button("Run"):
      #ops.wipe()
      JSONtoOPS(st.session_state.Model) #create model in openseespy
   
      for ivel in vel_list:
         
         runDinamicTrain(dictTrain[typeTrain]["lInt"], dictTrain[typeTrain]["listPz"], ivel, typeTrain, [zita_1/100, zita_2/100], [rail_1, rail_2], nodeOutput, [mode1_ref, mode2_ref], sFV = secondFV) #ANALISI DINAMICA 1
   
   with st.container(border=True):
      col1, col2, col3 = st.columns([1, 1, 1])
      with col1:   
         vectPlot = st.selectbox('Vector',(1, 2, 3, 4, 5, 6), index = 2)
         videoTrain = st.checkbox('video')
      with col2:  
         
         scaleVideo = st.number_input('scale', value=200, key="videoTrain_scale")
      with col3:  
         vel = st.selectbox('Velocity',vel_list)
      
      
      pathVideo_data = 'output_AnalisiDinamicaTreno/{}/v{}kmh/2_spostamento/disp_tag.txt'.format(typeTrain, vel)
      pathVideo = 'output_AnalisiDinamicaTreno/{}/v{}kmh/video.mp4'.format(typeTrain, vel)
      
      
      if st.button("Graph"):
         
         if videoTrain:
            Model_Animated(scaleVideo, pathVideo_data, pathVideo)
            video_file = open(pathVideo, 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)
         
         dictAcc = {}
         dictVel = {}
         dictDisp = {}
         for nodeTag in nodeOutput:
            pathAcc = 'output_AnalisiDinamicaTreno/{}/v{}kmh/0_accelerazione/acc_tag{}.txt'.format(typeTrain, vel, nodeTag)
            pathVel = 'output_AnalisiDinamicaTreno/{}/v{}kmh/1_velocita/vel_tag{}.txt'.format(typeTrain, vel, nodeTag)
            pathDisp = 'output_AnalisiDinamicaTreno/{}/v{}kmh/2_spostamento/disp_tag{}.txt'.format(typeTrain, vel, nodeTag)
            output_accPosAcc1 = PostData7column(pathAcc)
            output_velPosAcc1 = PostData7column(pathVel)
            output_dispPosAcc1 = PostData7column(pathDisp)
            dictAcc[nodeTag] = output_accPosAcc1[vectPlot]
            dictVel[nodeTag] = output_velPosAcc1[vectPlot]
            dictDisp[nodeTag] = output_dispPosAcc1[vectPlot]
         
         t = output_accPosAcc1[0]
         
         df_acc = pd.DataFrame(dictAcc, index = t)
         df_acc.index.name = "time"
         df_acc.columns.name = "nodeTag"
         
         df_vel = pd.DataFrame(dictVel, index = t)
         df_vel.index.name = "time"
         df_vel.columns.name = "nodeTag"
         
         df_disp = pd.DataFrame(dictDisp, index = t)
         df_disp.index.name = "time"
         df_disp.columns.name = "nodeTag"
         
         # Group data together
         fig_acc = px.line(
            df_acc, title='Acceleration',
            labels=dict(x='time [s]', y='acceleration [m/s^2]'),
            )

         st.plotly_chart(fig_acc, theme="streamlit", use_container_width=True)
         
         fig_vel = px.line(
            df_vel, title='Velocity',
            labels=dict(x='time [s]', y='velocity [m/s]'),
            )

         st.plotly_chart(fig_vel, theme="streamlit", use_container_width=True)
         
         fig_disp = px.line(
            df_disp, title='Displacement',
            labels=dict(x='time [s]', y='displacement [m]'),
            )

         st.plotly_chart(fig_disp, theme="streamlit", use_container_width=True)
         
         figSpectrum = trainSpectrum(df_acc, deltaT = 0.01)
         tab1, tab2 = st.tabs(["PSD", "FFT"])
         with tab1:
            # Use the Streamlit theme.
            # This is the default. So you can also omit the theme argument.
            st.plotly_chart(figSpectrum[1], theme="streamlit", use_container_width=True)
         with tab2:
            # Use the native Plotly theme.
            st.plotly_chart(figSpectrum[0], theme="streamlit", use_container_width=True)
            
      #EXSPERIMENTAL DATA
      with st.container(border=True):
         dataAccelerationJSON = st.file_uploader("Choose JSON file for experimental data", key="expAcc")
         #data =r"C:\Users\Domen\OneDrive\00_TOLS\GitHub\OPSdigitalTWIN\example\0_Travata metallica centrale\Sensore Ac.M-3-data-2024-04-23 18 14 21.csv"
         #pathexcData = st.text_input('Path experimental data', data, key = 'pathRealData')
         col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
         with col1:   
            shift = st.number_input('shift [s]', value=10.00, key="shiftAcc")
         with col2: 
            filterDown = st.number_input('filter_down', value=0.5, key="filter_1")
         with col3:
            filterUpper = st.number_input('filter_upp', value=10, key="filter_2")
         with col4:
            dataCompare = st.selectbox('Tag node for data compare', nodeOutput, index = 1)
         
         if dataAccelerationJSON is not None:
            spectra_df = pd.read_csv(dataAccelerationJSON)
            tSper, accSper, figDataSper =bandpass_filter(filterDown, filterUpper, spectra_df, dataKey = ['time', 'z ( g )'], scale = 9.8, shift = shift)
            figDataSper.name = "exsperimental"
            # Creazione del DataFrame FEM
            pathAcc = 'output_AnalisiDinamicaTreno/{}/v{}kmh/0_accelerazione/acc_tag{}.txt'.format(typeTrain, vel, dataCompare)
            output_accPosAcc = PostData7column(pathAcc)
            Acc = output_accPosAcc[vectPlot]
            t = output_accPosAcc[0]
            fem_df = pd.DataFrame({'time': t, 'valor': Acc})
            tFEM, accFEM, figDataFEM =bandpass_filter(filterDown, filterUpper, fem_df, dataKey = ['time', 'valor'], scale = 1, shift = 0)
            figDataFEM.name = "fem"
            # Creazione della figura
            figCompare = go.Figure()
            figCompare.add_traces(figDataSper)
            figCompare.add_traces(figDataFEM)  # Aggiungere le tracce della nuova figura alla figura esistente
            # Aggiornamento del layout della figura
            figCompare.update_layout(title='Confronto accelerazione', xaxis_title='time [s]', yaxis_title='acceleration [m/s^2]')
            st.plotly_chart(figCompare, theme="streamlit", use_container_width=True)
            
            ## SPETTRI
            df_accReal = pd.DataFrame({"acc": accSper}, index = tSper)
            df_accFem = pd.DataFrame({"acc": accFEM}, index = tFEM)
            figSpectrumReal = trainSpectrum(df_accReal, deltaT = 0.01)
            figSpectrumFem = trainSpectrum(df_accFem, deltaT = 0.01)
            tab1, tab2 = st.tabs(["PSD", "FFT"])
            with tab1:
               # Use the Streamlit theme.
               # This is the default. So you can also omit the theme argument.
               figCompare2 = go.Figure()
               # Configurazione dell'asse y con scala logaritmica
               figCompare2.update_yaxes(type='log')
               fig1 = go.Scatter(x=figSpectrumReal[2].index, y=figSpectrumReal[2]["acc"], name='exsperimental')
               fig2 = go.Scatter(x=figSpectrumFem[2].index, y=figSpectrumFem[2]["acc"], name='fem')
               figCompare2.add_traces(fig1)
               figCompare2.add_traces(fig2)  # Aggiungere le tracce della nuova figura alla figura esistente
               st.plotly_chart(figCompare2, theme="streamlit", use_container_width=True)
            with tab2:
               # Use the native Plotly theme.
               figCompare2 = go.Figure()
               fig1 = go.Scatter(x=figSpectrumReal[3].index, y=figSpectrumReal[3]["acc"], name='exsperimental')
               fig2 = go.Scatter(x=figSpectrumFem[3].index, y=figSpectrumFem[3]["acc"], name='fem')
               figCompare2.add_traces(fig1)
               figCompare2.add_traces(fig2)  # Aggiungere le tracce della nuova figura alla figura esistente
               st.plotly_chart(figCompare2, theme="streamlit", use_container_width=True)
            
            
                       
if selected3 == "WNoise":
   st.markdown("##### Rayleigh damping")
   with st.container():
      col1, col2 = st.columns([1, 1])
      with col1:
         mode1_ref = st.number_input('Mode 1', value=0, key="mode1_ref_WA")
         mode2_ref = st.number_input('Mode 1', value=1, key="mode2_ref_WA")
      with col2:
         dampingHelp = "steel bridge: 0.24-0.5; Prestressed concreate: 0.32-1.0; Reinforced concrerate bridge: 0.32-1.5"
         zita_1 = st.number_input('ζ1 [%]', value=0.4, key="zita1_WA", help=dampingHelp)
         zita_2 = st.number_input('ζ2 [%]', value=0.2, key="zita2_WA")
         
   # "Boundary Random"
   with st.container():
      st.markdown("##### Boundary Random Load")  
      with st.container():
         col1, col2 = st.columns([1, 1])
         with col1:
            bmin = st.number_input('load min', value=-0.0003*10000*128, key="Pmin")
         with col2:
            boundHelp = " "
            bmax = st.number_input('load max', value=0.0003*10000*128, key="Pmax")
      
      BoundLoad = [bmin, bmax] 
   
   # Recorder
   st.markdown("##### Node Load")
   with st.container():
      nodeLoad_tag = st.text_input('Node tag', [  1,   55,  281], key = 'NodeTag_WA')
   
   nodeLoad = [int(tag) for tag in nodeLoad_tag.strip('][').split(', ')]
      
   # Recorder
   st.markdown("##### Recorder Output")
   with st.container():
      col1, col2 = st.columns([1, 1])
      with col1:
         nodeRecorder = st.checkbox('Node Recorder', key = 'Node_Recorder_WA', help =" se vuoi salvare output nodali")
         nodeRecorder_tag = st.text_input('Node Recorder tag', [  7,   15,    10,  238,  240,   242], key = 'NodeRecorder_tag_WA')
      with col2:
         eleRecorder = st.checkbox('Ele Recorder (W.I.P.)', key = 'Ele_Recorder_WA', help =" se vuoi salvare output degli elementi")
         eleRecorder_tag = st.text_input('Ele Recorder tag (W.I.P.)', [  7,   15,    10,  238,  240,   242], key = 'EleRecorder_tag_WA')
   
   nodeOutput = [int(tag) for tag in nodeRecorder_tag.strip('][').split(', ')]
   eleOutput = [int(tag) for tag in eleRecorder_tag.strip('][').split(', ')]
         
   # Input Analisys
   st.markdown("##### Analisys input")
   with st.container():
      col1, col2 = st.columns([1, 1])
      with col1:
         secondFV = st.number_input('secondi', value=20, key="sFV", help = "durata oscillazioni (deltaT = 0.01)")
         timeStep = 0.01
         nStep = int(secondFV/0.01)
         st.write('Number of step is ', nStep)
         
      noiseList = defineWNoise(BoundLoad, len(nodeLoad), nStep)
      xWN = [i for i in range(0,nStep)]
      
      if st.button("ViewLoad", key="viewNoise"):
         fig = go.Figure()
         for i in noiseList:
            # Create traces
            fig.add_trace(go.Scatter(x=xWN, y=i,))
         st.plotly_chart(fig, use_container_width=True)
         
      
   if st.button("Run", key="RunWNoise"):
      #ops.wipe()
      JSONtoOPS(st.session_state.Model) #create model in openseespy
      teta = [zita_1, zita_2]
      runAnalisiAmbientale(teta, noiseList, nodeLoad, nodeOutput, nStep, timeStep, name = "prova", fIndex = [int(mode1_ref), int(mode2_ref)])  
   
   pathVideo_data = 'output_AnalisiAmbientale/{}/Step_{}/2_spostamento/disp_tag.txt'.format("prova",nStep)
   pathVideo = 'output_AnalisiAmbientale/{}/Step_{}/video.mp4'.format("prova",nStep)
      
   #EXSPERIMENTAL DATA
   with st.container(border=True):
      col1, col2= st.columns([1, 1])
      with col1:   
         videoAmb = st.checkbox('video')
      with col2:  
         scaleVideo = st.number_input('scale', value=200, key="videoAmb_scale")
         
      if st.button("Graph"):
         if videoAmb:
            Model_Animated(scaleVideo, pathVideo_data, pathVideo)
            video_file = open(pathVideo, 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)
            
if selected3 == "Quake":
   with st.expander("Response Spectrum Analysis"):
      st.latex(r''' U_{ij}^n = \frac{\Phi_{ij}^n \cdot MPF_{ij} \cdot RSf\left(T_i\right)}{\lambda_i} ''')
      
      st.markdown("Inserire un file excel per definire lo spettro di risposta")
      # Caricamento del file Excel tramite widget di Streamlit
      fileSpectrum = st.file_uploader("Carica file Excel", type=["xlsx", "xls"], key="Spectrum")

      if fileSpectrum is not None:
         # Leggi il file Excel usando Pandas
         excelSpectrum_data = pd.read_excel(fileSpectrum, sheet_name=None)
         st.session_state["Spectrum_xy"] = pd.read_excel(fileSpectrum, sheet_name="Sxy")
         st.session_state["Spectrum_z"] = pd.read_excel(fileSpectrum, sheet_name="Sz")
         
         try:
            # Tracciamento dei dati con Plotly per Sxy
            fig_spectrum = go.Figure()
            fig_spectrum.add_trace(go.Scatter(x=st.session_state["Spectrum_xy"]["T"], y=st.session_state["Spectrum_xy"]["Sa"], mode='lines+markers', name='Spectrum_xy'))
            
            # Tracciamento dei dati con Plotly per Sz
            fig_spectrum.add_trace(go.Scatter(x=st.session_state["Spectrum_z"]["T"], y=st.session_state["Spectrum_z"]["Sa"], mode='lines+markers', name='Spectrum_z'))
            fig_spectrum.update_layout(title='Spectrum',
                                 xaxis_title='T',
                                 yaxis_title='Sa')
            st.plotly_chart(fig_spectrum)
         except:
            pass

      col1, col2= st.columns([1, 1])
      with col1:
         dt = st.number_input('dt', 0.01, key = 'dt_Spectrum')
      with col2:
         dirAcc = st.multiselect('direction',[1, 2, 3, 4, 5, 6],[1, 2, 3, 4, 5, 6], key="dirSpectrum")

      col1, col2= st.columns([1, 1])
      with col1:  
         runSpectrum = st.button("Run")
      with col2:  
         sviewresult_spectrum = st.button("View")
      
      st.markdown("## W.I.P.")


   
   with st.expander("Dynamic Analysis with Accelerogram"):
      st.markdown("Inserire un file excel per definire gli accelerogrammi")
      # Caricamento del file Excel tramite widget di Streamlit
      fileAcc = st.file_uploader("Carica file Excel", type=["xlsx", "xls"], key="accData")
      # NodeLoad
      st.markdown("##### Load Params")
      with st.container():
         col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
         with col1:
            dt = st.number_input('dt', 0.01, key = 'dt_QuakeAcc')
         with col2:
            dirAcc = st.multiselect('direction',[1, 2, 3, 4, 5, 6],[1, 2, 3, 4, 5, 6], key="dirAcc")
         with col3:   
           type_bounds = st.selectbox('boundsLoad', ["boundary", "Node define"], key = 'boundsLoad_QuakeAcc')
         with col4:
            nodeLoad_tag = st.text_input('Node tag', [1,   55,  281], key = 'NodeTag_QuakeAcc')
      
      nodeLoad = [int(tag) for tag in nodeLoad_tag.strip('][').split(', ')]
         
      # Recorder
      st.markdown("##### Recorder Output")
      with st.container():
         col1, col2 = st.columns([1, 1])
         with col1:
            nodeRecorder = st.checkbox('Node Recorder', key = 'Node_Recorder_WA', help =" se vuoi salvare output nodali")
            nodeRecorder_tag = st.text_input('Node Recorder tag', [  7,   15,    10,  238,  240,   242], key = 'NodeRecorder_tag__QuakeAcc')
         with col2:
            eleRecorder = st.checkbox('Ele Recorder (W.I.P.)', key = 'Ele_Recorder_WA', help =" se vuoi salvare output degli elementi")
            eleRecorder_tag = st.text_input('Ele Recorder tag (W.I.P.)', [  7,   15,    10,  238,  240,   242], key = 'EleRecorder_tag__QuakeAcc')
      
      nodeOutput = [int(tag) for tag in nodeRecorder_tag.strip('][').split(', ')]
      eleOutput = [int(tag) for tag in eleRecorder_tag.strip('][').split(', ')]
      
      col1, col2= st.columns([1, 1])
      with col1:  
         runSpectrum = st.button("Run", key= "run_quakeAcc")
      with col2:  
         sviewresult_spectrum = st.button("View", key = "view_quakeAcc")
      
      st.markdown("## W.I.P.")

      
## VIEW MODAL RESULT  
if selected3 == "Other":
   #ops.wipe()
   try:
      JSONtoOPS(st.session_state.Model) #create model in openseespy
   except:
      st.warning('Problemi con la crezione del modello in Opensees' , icon="⚠️")
   
   with st.expander("Modal Analysis"):
      st.markdown("Result of Modal Analysis")
      st.latex(r''' [K] = \{\lambda\} [M] ''')
      
      number = st.number_input("Insert number of modes", value=12, min_value = 1, step = 1, key = "numberModes")
      if st.button("Run", key="runModale"):
         #Mplus = {"1":{"tag": [1,32], "mass":0.785},
         #   "2":{"tag": [5,9,13,17,21,25,29], "mass": 0.21},
         #}
         Mplus = False
         fM = OPS_Modal(number, Mplus = Mplus, recorder = True, printOut = False, reportFileName = False)
         st.session_state["frequencyModal"] = fM
         OutputModal = ops.modalProperties('-return', '-unorm') #pd.DataFrame(
         del OutputModal['domainSize']
         st.session_state["propModal"] = OutputModal
         # Define Static Analysis
         ops.timeSeries('Linear', 1)
         ops.pattern('Plain', 1, 1)
         ops.analysis('Static')

         #Run Analysis
         ops.analyze(1)
      
         
      st.markdown("Modal Parameter")
      try:
         st.json(st.session_state.propModal, expanded = False)
      except:
         pass
      ops.wipeAnalysis()
         
      #if st.button("View", key="viewModalPlot"):
      modalFigView = st.slider('View modes', 1, number, 2)     
      #plot
      toggleViewMS = st.toggle(label='Activate view', key="viewMS", value=False)
      if toggleViewMS:
         try:
            figModalPlot = opsModel_Plot3d_defModal(st.session_state.Model, modalFigView, round(st.session_state.frequencyModal[modalFigView-1],3), path = '', ViewModel = False)
         except:
            figModalPlot = opsModel_Plot3d_defModal(st.session_state.Model, modalFigView, fM= [], path = '', ViewModel = False)
         
         stpyvista(figModalPlot, panel_kwargs=dict(orientation_widget=True)) 
         
   with st.expander("Bucking Analysis"):
      st.markdown("Result of Bucking Analysis")
      st.latex(r''' [K] = \{\lambda\} [M]''')
      
      try:
         optionsLPBL = st.multiselect('Load Pattern for Bucking Load',
         st.session_state["Load"]["LoadPattern"]["Name"].tolist(),
         st.session_state["Load"]["LoadPattern"]["Name"].tolist()[0])
      
         scaleLPBL = [1 for i in optionsLPBL]
      except:
         st.warning('Non è stato caricato il file dei carichi' , icon="⚠️")
      
      
      
      if st.button("Run", key = "runBucking"):
         JSONtoOPS(st.session_state.Model, bucking=True) #create model in openseespy
         modShapeBucking = runAnalisiBucking(st.session_state.Model, st.session_state["Load"], optionsLPBL, scaleLPBL, write=False)
         st.session_state["buckingShape"] = modShapeBucking
      
      
      nBM = st.slider('View modes', 1, number, 2, key = "buckingShapeView")
      #if  st.session_state.buckingShape is not None:
      toggleViewBM = st.toggle(label='Activate view', key="viewBMS", value=False)
      if toggleViewBM:
         figBMPlot = plotBucking(st.session_state.Model, st.session_state.buckingShape, nBM)
         stpyvista(figBMPlot, panel_kwargs=dict(orientation_widget=True))
         
      
   with st.expander("Static Analysis"):
      st.markdown("Result of Static Analysis")
      st.latex(r'''[A]\{x\} = \{b\}''')
      
      try:
         lpList = list(st.session_state.Model["StructuralAnalysisModel"]["beam load"].keys())
         #st.session_state["Load"]["LoadPattern"]["Name"].tolist()
         lpList.append("All")
         optionLP = st.selectbox("load Pattern to Run", lpList)
      except:
         st.warning('Non è stato caricato il file dei carichi' , icon="⚠️")
  
      if st.button("Run", key = "runStatic"):
         ops.wipe()
         JSONtoOPS(st.session_state.Model)
         my_bar = st.progress(0, text="Static Analyze in progress. Please wait")
         percent_complete = 0
         if optionLP == "All":
            for iLP in  lpList[0:-2]:
               st.write("Analyze {}".format(iLP))
               runStaticAnalysis(iLP, st.session_state.Model)
               percent_complete = percent_complete + 1
               my_bar.progress(percent_complete, text="Finish Analyze {}".format(iLP))
               ops.wipeAnalysis()
               
         else:
            runStaticAnalysis(optionLP, st.session_state.Model)
            percent_complete = percent_complete + 1
            my_bar.progress(percent_complete, text="Finish Analyze {}".format(optionLP))
            ops.wipeAnalysis()
         
         my_bar.empty()
         
      toggleViewStatic = st.toggle(label='Activate view', key="viewStatic", value=False)
      if toggleViewStatic:
         try:
            figStaticPlot = opsModel_Plot3d_defStatic(st.session_state.Model, optionLP)
            stpyvista(figStaticPlot, panel_kwargs=dict(orientation_widget=True)) 
         except:
            st.warning("Probabilmente non è stata svolta l'analisi per questo caso di carico" , icon="⚠️")