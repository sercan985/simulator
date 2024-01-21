import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

def graph_visualize(time, particle_count_per_tick, PROC_TICKS):

    x = [i for i in range(PROC_TICKS + 1) for j in range(particle_count_per_tick[i - 1])]

    # Y axis
    y = [particle[0] for i in time for particle in i]

    # Velocities
    vel_list = [particle[1] for i in time for particle in i]

    # Masses
    mass_list = [particle[2] for i in time for particle in i]

    # Create scatter plot
    df = px.data.iris()
    fig = px.scatter(df, x=x, y=y, size=list(mass_list), color= vel_list)

    fig.update_xaxes(title_text='time')

    # Update y-axis label
    fig.update_yaxes(title_text='pos')
    fig.update_layout(title_text='Allah Simulation')

    fig.show()