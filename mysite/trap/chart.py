import matplotlib
matplotlib.use('Agg')
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image
from io import BytesIO

def create_chart(request,x,y,x_label,y_label,chart_title):
    # Construct the graph

    plot(x, y, linewidth=1.0)

    xlabel(x_label)
    ylabel(y_label)
    title(chart_title)
    grid(True)

    # Store image in a buffer
    buffer = BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()
    content_type="image/png"
    # Send buffer in a http response the the browser with the mime type image/png set
    return buffer.getvalue(), content_type
