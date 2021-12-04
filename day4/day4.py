with open("input", "r") as f:
    numbers = list(map(int, f.readline().strip().split(",")))
    lines = [list(map(int, line.split())) for line in f.readlines() if line.strip()]

rows = lines

columns = []
for i in range(len(rows[0])):
    columns.append([row[i] for row in rows])
columns = [column[i:i+5] for i in range(0, len(columns[0]), 5) for column in columns]

def part_a():
    checked_numbers = []
    def get_winning_lineindex():
        for num in numbers:
            checked_numbers.append(num)

            for row in rows:
                row_count = 0
                for cnum in checked_numbers:
                    if cnum in row:
                        row_count += 1
                        if row_count == 5:
                            print("Took row path")
                            return row
            
            for column in columns:
                column_count = 0
                for cnum in checked_numbers:
                    if cnum in column:
                        column_count += 1
                        if column_count == 5:
                            print("Took column path")
                            return column

    winner = get_winning_lineindex()

    print(f"{winner=}")
    print(f"{checked_numbers=}")

    def get_winning_board(lineindex):
        if lineindex[1] == "r":
            return [rows[i] for i in range(len(rows)) if int(i / 5) == int(lineindex[0] / 5)]
        else:
            return [columns[i] for i in range(len(columns)) if int(i / 5) == int(lineindex[0] / 5)]

    winning_bord = get_winning_board( (columns.index(winner), "c") if winner in columns else (rows.index(winner), "r") )
    print(f"{winning_bord=}")
    
    unmarked_numbers = [unmarked_num for item in winning_bord for unmarked_num in item if unmarked_num not in checked_numbers]
    print(f"{unmarked_numbers=}")
    return sum(unmarked_numbers) * checked_numbers[-1]

print(part_a())