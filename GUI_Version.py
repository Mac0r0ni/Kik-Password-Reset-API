from tkinter import *
import requests

root = Tk()
root.title("Kik Password Reset")
root.configure(background='black')
label_emailOrUsername = Label(root, text="EMAIL OR USERNAME", bg="black", fg="green")
get_emailOrUsername = Entry(root, bg="black", fg="green")
blank_space = Label(root, text="", bg="black", fg="green")
blank_space = Label(root, text="", bg="black", fg="green")
label_emailOrUsername.grid(column=0, row=0)
get_emailOrUsername.grid(column=0, row=1)
blank_space.grid(column=0, row=2)

def reset_password():
  newWindow = Toplevel(root)
  newWindow.title("Result")
  newWindow.configure(background='black')
  emailOrUsername = get_emailOrUsername.get()
  
  def post_text(string):
    Label(newWindow, text=string, fg="green", bg="black").pack()

  try:
    if emailOrUsername == "":
      post_text("PLEASE ENTER AN EMAIL OR USERNAME")
      return
    else:
      print("Resetting password, please wait...")
      url = 'https://KPR-API.stethosayshello.repl.co'
      payload = { 'emailOrUsername' : str(emailOrUsername) }
      res = requests.post(url, data=payload)
      result = str(res.content)
      result = result[18:-7]
      # The API returns raw results from ws.kik.com, which tends to have some odd formatting. 
      # The below 4 lines is just to remove that formatting.
      result = result.replace("\n", " ")
      result = result.replace("\\", "")
      while "  " in result:
        result = result.replace("  ", " ")
      print("Posting result in new window.")
      split_strings = []
      n  = 40
      for index in range(0, len(result), n):
        split_strings.append(result[index : index + n])
      for string in split_strings:
        post_text(string)
  except:
    post_text("Something went wrong!")

resetButton = Button(root, text="RESET PASSWORD", padx=70, pady=10, command=reset_password, fg="black", bg="green", highlightthickness=0, activebackground="green")
resetButton.grid(column=0, row=3)

root.mainloop()
