from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import BSPlotter
import matplotlib.pyplot as plt
import re


def format_label(label):
    label = label.replace("\\Gamma", r"\Gamma")

    m = re.match(r"([A-Za-z]+)_([0-9]+)", label)
    if m:
        return rf"${m.group(1)}_{{{m.group(2)}}}$"

    return rf"${label}$"

# ------------------ GLOBAL STYLE ------------------
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.linewidth": 1.5,
    "xtick.major.width": 1.5,
    "ytick.major.width": 1.5,
})

# ------------------ READ BAND STRUCTURE ------------------
vasprun = Vasprun(
    "vasprun.xml",
    parse_projected_eigen=False
)

bs = vasprun.get_band_structure(
    line_mode=True)

# ------------------ PLOT ------------------
### This line is the one doing the plot :)
plotter = BSPlotter(bs)


tick_positions = []
tick_labels = []

i = 0

### Managing the labels of the band structure
while i < len(bs.kpoints):

    k = bs.kpoints[i]

    if k.label is not None:

        label = k.label.replace("\\Gamma", "Γ")
        # Convert H_0 -> $H_0$, S_2 -> $S_2$, etc.
        label = re.sub(r'([A-Za-z]+)_([0-9]+)', r'$\1_{\2}$', label)

        # Check if next labeled point is at same distance
        if (
            i < len(bs.kpoints) - 1
            and bs.kpoints[i + 1].label is not None
            and abs(bs.distance[i + 1] - bs.distance[i]) < 1e-6
        ):

            next_label = bs.kpoints[i + 1].label.replace("\\Gamma", "Γ")
            next_label = bs.kpoints[i + 1].label
            if next_label == "\\Gamma":
                next_label = "Γ"

            next_label = format_label(next_label)
            label = f"{label}|{next_label}"


            tick_positions.append(bs.distance[i])
            tick_labels.append(label)

            i += 2
            continue

        tick_positions.append(bs.distance[i])
        tick_labels.append(label)

    i += 1

print(tick_labels)

### End of managing labels of the band structure


### Formatting figure
ax = plotter.get_plot()

# Take off legend
legend = ax.get_legend()
if legend is not None:
    legend.remove()

### Modifying size of figure and line widths.
fig = ax.figure
fig.set_size_inches(14, 8)
for line in ax.get_lines():
    line.set_linewidth(3.5) # line width

ax.set_xticks(tick_positions)
ax.set_xticklabels(tick_labels)

for x in tick_positions:
    ax.axvline(x, color="gray", lw=0.5, alpha=0.5)

ax.set_ylim(-4, 4) # Energy window (vertical axes limits)

ax.set_ylabel("Energy (eV)")

plt.savefig(
    "band_structure.pdf", # name of generated figure 
    dpi=600,
    bbox_inches="tight"
)

plt.close()
