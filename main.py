#Lyrical Visualizer
#Calli Gilbert-Neel 03/11/2026
####test run code :text = ""
#result = te.get_emotion(text)

#print("Emotion Analysis:")
#for emotion, score in result.items():
    #print(f"- {emotion}: {score * 100}%")



#import text2emotion library and nickname it
import text2emotion as te
##import plotting tool of matplotlib and nickname it
import matplotlib.pyplot as plt

#function for taking user input and assigning the basic emotion vis text2emotion and assign basic starting emotion
def get_emotions(text):
    emotions = te.get_emotion(text)
    return {
        "Happy":  emotions.get("Happy", 0),
        "Sad":    emotions.get("Sad", 0),
        "Angry":  emotions.get("Angry", 0),
    }

#Chart functions using matplotlib-assigning colors for happy-yellow,sad-blue,mad-red
def visualize_emotions(text):
    emotions = get_emotions(text)

    labels = list(emotions.keys())
    values = list(emotions.values())
    colors = ["#F5C842", "#5B8FD4", "#D45B5B"]  # yellow, blue, red
#defining chart size and color
    fig, ax = plt.subplots(figsize=(7, 4))
    fig.patch.set_facecolor("#1E1E2E")
    ax.set_facecolor("#1E1E2E")
#drawing bars for chart and connecting them to proper labels, and zorder=3 makes sure it lays over the lines in chartproperly
    bars = ax.bar(labels, values, color=colors, width=0.5, zorder=3)

#a for loop as it adds the emotion value, labels on top of each bar, positions/centers bar/text and adds color/size, 
    for bar, val in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.02,
            f"{val:.2f}",
            ha="center", va="bottom",
            color="white", fontsize=12, fontweight="bold"
        )
#sets y axis max-min
    ax.set_ylim(0, 1.15)
#side of chart label
    ax.set_ylabel("Score", color="white", fontsize=11)
#Bottom chart label
    ax.set_title("Emotion Analysis", color="white", fontsize=15, fontweight="bold", pad=15)


#removing border lines adding white  grid lines
    ax.tick_params(colors="white", labelsize=12)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.yaxis.grid(True, color="white", alpha=0.1, zorder=0)
    ax.set_axisbelow(True)


#automatically djusts spacing so nothing gets cut off.
    plt.tight_layout()

#pops up chart!
    plt.show()
#file connection, asks for user input and runs visiualization function
if __name__ == "__main__":
    user_text = input(" What is one sentence from your favorite song? ")
    visualize_emotions(user_text)
