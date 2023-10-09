from dash import Dash, html, dcc, callback, Output, Input
# import dash_bootstrap_components as dbc
# import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import sqlalchemy as sa

SERVER_NAME = '5CG2218ZB6\SQL19V'
DB = 'MITS'

engine = sa.create_engine('mssql+pyodbc://{server}/{db}?driver=ODBC Driver 17 for SQL Server'.format(server=SERVER_NAME, db=DB))
connection = engine.connect()
df = pd.read_sql('SELECT TOP (5) * FROM VA_2023..VA2023', connection)
data_dict = df.set_index('Adssid').to_dict()
print(data_dict)
mits_id = 682739 #input("Please enter the study ID here: ") # Test Ids 597320 600982
print(f"The Age show is for {mits_id}: ", mits_id)
print(data_dict['name']['{mitsid}'.format(mitsid=mits_id)])
# Column 1 Information
def col1(): 
    return html.Div(
                    className='col',
                    children=[
                        html.Div(
                        children=[
                            # html.Aler('Display DataFrame'),
                            html.Div(html.H2("Deceased Infomation", className='alert alert-primary'), style={}),
                            html.P("Demogragraphic Information about {id_died}".format(id_died=mits_id), style={'text-decoration': 'underline'}),
                            html.Div(
                                className="card mt-3 ",
                                children = [
                                    html.Div(
                                    className='cardbody',
                                    children=[   
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(children=[html.P("STUDY ID", style={'text-align': 'left'})],className='col'),
                                            html.Div(children=[html.P("{id_died}".format(id_died=mits_id), style={'text-align': 'left'})],className='col',),
                                            ],
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Age", style={'text-align': 'left'}),className='col', ),
                                            html.Div(html.P(data_dict['Age']['{mitsid}'.format(mitsid=mits_id)], style={'text-align': 'left'}), className='col',),
                                            ],
                                            
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Date of birth", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['Dob']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Date of death", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['Dod_1']['{mitsid}'.format(mitsid=mits_id)], style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Gender", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['Sex']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Day of death?", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['WeekDay']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Marital Status", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['Marital']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Citizenship/Nationality", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['Nationality']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Ethnicity", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['Ethnicity']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Death place", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['death_place_region']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Highest level of schooling", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['education_level']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Occupation", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['Occupation']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Economic activity status", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['Economic_Act']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Was literate", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['read_write']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                    ]
                                    
                                )],
                                style = {'background-color':'#fafbfe'}
                            )
                        ]
                    )
                    ],
                    style = {'background-color':'#f5f8fe'}
                    
                )


# Column 2 Information
def col2(): 
    return html.Div(
                    className='col',
                    children=[
                    html.Div(
                        [
                            # html.H1('Other Content'),
                            html.Div(className='alert alert-primary', children=[html.H2("Respondent Infomation")],),
                            html.P("This is some other content in ", style={'text-decoration': 'underline'}),
                            html.Div(
                                className="card mt-3 ",
                                children = [
                                html.Div(
                                    className='cardbody',
                                    children=[   
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Age", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['resp_age']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Relationship to the deceased", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['Relationship_to_deceased']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Live with the deceased", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['LiveWith']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Member of the household of deceased", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['same_dwelling']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Gender", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['resp_sex']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Date of Birth", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['resp_dob']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        
                                    ]
                                )],
                                style = {'background-color':'#fafbfe'}
                            )
                        ]
                    )
                    ],
                    style = {'background-color':'#f5f8fe'}
                )

# Column 3 Information
def col3(): 
    return html.Div(
                    className='col',
                    children=[
                    html.Div(
                        [
                            # html.H1('Other fddd'),
                            html.Div(className='alert alert-primary', children=[html.H2("Interview Quentions")],),
                            html.P([html.A("All questions about",href="#"), html.A(" symtopms & causes the death",href="#")], style={'text-decoration': 'underline'}),
                            html.Div(
                                className="card mt-3 ",
                                children = [
                                html.Div(
                                    className='cardbody',
                                    children=[   
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Open narrative", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(str(data_dict['Narrative']['{mitsid}'.format(mitsid=mits_id)])
                                                           ,style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Family Declared Cause of death",style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['FamCause1']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Causes of Death: List", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(str(data_dict['narrative_1']['{mitsid}'.format(mitsid=mits_id)]) + " "+
                                                           str(data_dict['narrative_2']['{mitsid}'.format(mitsid=mits_id)]) + " "+
                                                           str(data_dict['narrative_3']['{mitsid}'.format(mitsid=mits_id)])
                                                           ,style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Did (s)he suffer from any injury or accident that led to her/his death?", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['Injury']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Do you think s/he committed suicide?", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['Suicide']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Was there any poisoning?", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['Poison']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Did (s)he die of drowning?", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['Drown']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Was (s)he injured by a bite or sting by venomous animal?", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['Vemon_suffer_from']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Was (s)he injured by burns/fire?", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['Fire']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Was (s)he subject to violence (suicide, homicide, abuse)?", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['Assault']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Was (s)he injured by a fire arm?", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['Firearm']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Was (s)he stabbed, cut or pierced?", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['Stab']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Was s/he injured by machinery?", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['Machinery']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            className='row',
                                            children=[
                                            html.Div(html.P("Was the HIV test ever positive?", style={'text-align': 'left'}), className='col',),
                                            html.Div(html.P(data_dict['hiv_pos']['{mitsid}'.format(mitsid=mits_id)],style={'text-align': 'left'}), className='col',),
                                            ]
                                        ),
                                    ]
                                )],
                                style = {'background-color':'#fafbfe'}
                            )
                        ]
                    )],
                    style = {'background-color':'#f5f8fe'}
                )


