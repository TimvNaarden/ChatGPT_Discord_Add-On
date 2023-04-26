from discord.ext import commands
import openai
import textwrap


class CommandsCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.prompt = []
        self.response = ""
        self.answer = ""
        self.wraplength = 2000

    def get_answer(self, question) -> str:
        self.prompt.append({"role": "user", "content": f"{question}"})

        try:
            self.response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.prompt
            )
        except Exception as e:
            print(e)

        return self.response["choices"][0]["message"]["content"]

    # Define an event handler for when a message is sent
    @commands.command(name="chatgpt", aliases=["ask"], help="Ask chatgpt an question")
    async def chatgpt(self, ctx, *args):
        question = " ".join(args)
        print(f"{ctx.author} asked {question}")
        self.answer = self.get_answer(question)

        for line in textwrap.wrap(self.answer, self.wraplength):
            await ctx.send(line)

    @commands.command(name="clear", aliases=["c", "bin"], help="Clears the conversation")
    async def clear(self, ctx):
        self.prompt = []
        await ctx.send("Conversation cleared successfully")


async def setup(bot):
    await bot.add_cog(CommandsCog(bot))
