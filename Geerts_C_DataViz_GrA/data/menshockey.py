import csv
import matplotlib.pyplot as pyplot

gold = []
silver = []
bronze = []

categories = []

with open('menshockey.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		else:
			if row[7] == "Gold":
				print("won gold!")
				gold.append(row[7])

			if row[7] == "Gold":
				print("won silver.")
				silver.append(row[7])

			if row[7] == "Bronze":
				print("won bronze.")
				bronze.append(row[7])

			line_count += 1

		print("gold medals: ", len(gold))
		print("silver medals: ", len(silver))
		print("bronze medals: ", len(bronze))

		# plot as a pie chart
		labels = ("Gold", "Silver", "Bronze")

		sizes = [len(gold), len(silver), len(bronze)]
		colors = ['gold', 'silver', 'darkgoldenrod'] 
		explode = (0.1, 0, 0)

		plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
		plt.axis('equal')
		plt.legend(labels, loc=1)
		plt.title("Gold Medals For Men's Hockey")
		plt.xlabel("Medals since 1924")
		plt.show()
		
