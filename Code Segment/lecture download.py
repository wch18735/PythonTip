import requests

if __name__=="__main__":
    with open("./lecture.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]

        file_order = 1
        week = ""
        for line in lines:
            # len(https) == 5
            if len(line) < 5:
                week = line
                file_order = 1
                continue

            # process print
            print(f"{week}({file_order}).mp4 download start!")

            # get request from url
            r = requests.get(line)
            with open("C:/Users/wch18/Downloads/" + f"{week}({file_order}).mp4", "wb") as video:
                video.write(r.content)

            # print processed
            print(f"{week}({file_order}).mp4 finish!")

            # plus file order
            file_order += 1