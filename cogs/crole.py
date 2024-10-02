import discord
from discord import ButtonStyle, Interaction, app_commands
from discord.ext import commands
from discord.ui import Button, View, button

from config.config import config


async def add_or_remove_role(roleId: int, interaction: Interaction):
    role = interaction.guild.get_role(roleId)
    if role in interaction.user.roles:
        await interaction.user.remove_roles(role)
        await interaction.response.send_message(
            f"{role.mention} を解除しました", ephemeral=True
        )
    else:
        await interaction.user.add_roles(role)
        await interaction.response.send_message(
            f"{role.mention} を付与しました", ephemeral=True
        )


class CRoleRankButtons(View):  # コマンダーランク
    def __init__(self):
        super().__init__(timeout=None)

    @button(label="駆け出し", style=ButtonStyle.gray, emoji="🇦", custom_id="start-dash")
    async def pressedCom1(self, interaction: Interaction, button: Button):
        await add_or_remove_role(965084663855063040, interaction)

    @button(label="初級", style=ButtonStyle.blurple, emoji="🇧", custom_id="beginner")
    async def pressedCom2(self, interaction: Interaction, button: Button):
        await add_or_remove_role(738936069428478013, interaction)

    @button(label="中級", style=ButtonStyle.red, emoji="🇨", custom_id="intermediate")
    async def pressedCom3(self, interaction: Interaction, button: Button):
        await add_or_remove_role(965084054204608582, interaction)

    @button(label="上級", style=ButtonStyle.green, emoji="🇩", custom_id="advanced")
    async def pressedCom4(self, interaction: Interaction, button: Button):
        await add_or_remove_role(965084145644601344, interaction)


class CRoleJEBEButtons(View):  # JE or BE & 遊んでる機種
    def __init__(self):
        super().__init__(timeout=None)

    @button(
        label="JE勢",
        style=ButtonStyle.green,
        emoji="<:JE:892256704123772931>",
        row=0,
        custom_id="java",
    )
    async def pressedJebe1(self, interaction: Interaction, button: Button):
        await add_or_remove_role(744471714574106664, interaction)

    @button(
        label="BE勢",
        style=ButtonStyle.blurple,
        emoji="<:BE:892256680509861929>",
        row=0,
        custom_id="bedrock",
    )
    async def pressedJebe2(self, interaction: Interaction, button: Button):
        await add_or_remove_role(744471657061548223, interaction)

    @button(label="PC", style=ButtonStyle.gray, emoji="🖥️", row=1, custom_id="computer")
    async def pressedJebe3(self, interaction: Interaction, button: Button):
        await add_or_remove_role(1103559576953045042, interaction)

    @button(
        label="スマホ", style=ButtonStyle.gray, emoji="📱", row=1, custom_id="smartphone"
    )
    async def pressedJebe4(self, interaction: Interaction, button: Button):
        await add_or_remove_role(1103559803827146823, interaction)

    @button(
        label="家庭用ゲーム機", style=ButtonStyle.gray, emoji="🎮", row=1, custom_id="console"
    )
    async def pressedJebe5(self, interaction: Interaction, button: Button):
        await add_or_remove_role(1103559906872795178, interaction)


class CRoleAdButtons(View):  # 宣伝関連 & 質問メンション
    def __init__(self):
        super().__init__(timeout=None)

    @button(
        label="宣伝し隊", style=ButtonStyle.green, emoji="📝", row=0, custom_id="ads-sender"
    )
    async def pressedSen1(self, interaction: Interaction, button: Button):
        await add_or_remove_role(808617738180231178, interaction)

    @button(
        label="宣伝ウェルカム",
        style=ButtonStyle.blurple,
        emoji="📩",
        row=0,
        custom_id="ads-welcome",
    )
    async def pressedSen2(self, interaction: Interaction, button: Button):
        await add_or_remove_role(808618017247330324, interaction)

    @button(
        label="DM質問OK",
        style=ButtonStyle.red,
        emoji="📮",
        row=0,
        custom_id="dm-question-ok",
    )
    async def pressedSen5(self, interaction: Interaction, button: Button):
        await add_or_remove_role(972312252889837598, interaction)

    @button(
        label="JE-質問メンション可",
        style=ButtonStyle.gray,
        emoji="<:JE:892256704123772931>",
        row=1,
        custom_id="je-mention",
    )
    async def pressedSen3(self, interaction: Interaction, button: Button):
        await add_or_remove_role(888048122616500224, interaction)

    @button(
        label="BE-質問メンション可",
        style=ButtonStyle.gray,
        emoji="<:BE:892256680509861929>",
        row=1,
        custom_id="be-mention",
    )
    async def pressedSen4(self, interaction: Interaction, button: Button):
        await add_or_remove_role(888048127699996712, interaction)


class CRoleOtherButtons(View):  # その他
    def __init__(self):
        super().__init__(timeout=None)

    @button(label="通知ON", style=ButtonStyle.gray, emoji="🔔", custom_id="notify-ok")
    async def pressedHoka1(self, interaction: Interaction, button: Button):
        await add_or_remove_role(763342542719811605, interaction)

    @button(
        label="MEE6レベル無効化", style=ButtonStyle.gray, emoji="🔏", custom_id="disable-mee6"
    )
    async def pressedHoka2(self, interaction: Interaction, button: Button):
        await add_or_remove_role(891286619783581706, interaction)

    @button(label="FOREVER_18", style=ButtonStyle.gray, emoji="🔞", custom_id="r18")
    async def pressedHoka3(self, interaction: Interaction, button: Button):
        await add_or_remove_role(892062948531523665, interaction)

    @button(label="bump非表示", style=ButtonStyle.gray, emoji="⤴️", custom_id="no-bump")
    async def pressedHoka5(self, interaction: Interaction, button: Button):
        await add_or_remove_role(873890138063794236, interaction)


class CRole(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="crole", description="【運営】ロール付与するボタンを表示させるコマンドです)")
    @app_commands.checks.has_role(config.administrater_role_id)
    async def croll(self, interaction: Interaction):
        role_embed = discord.Embed(
            title="ロール設定",
            description="該当するロールのボタンを押すと付与されます\nもう一度押すと、解除されます",
            color=0x3AFF11,
        )
        com_embed = discord.Embed(
            title="コマンダーランク設定", description="ーーーーーーーーーー", color=0x3AFF11
        )
        com_embed.add_field(
            name="--【@駆け出しコマンダー】--", value="🇦:興味を持っている/これから勉強を始める方はこちら!", inline=False
        )
        com_embed.add_field(
            name="--【@初級コマンダー】--",
            value="🇧:少しでもコマンドができる人はこちら!\n(tp,gamemode,weather,etc.)",
            inline=False,
        )
        com_embed.add_field(
            name="--【@中級コマンダー】--",
            value="🇨:まぁまぁできるかなという方やある程度のアイテムを作れるなどという方はこちら!\n(scoreboard,execute,etc.)",
            inline=False,
        )
        com_embed.add_field(
            name="--【@上級コマンダー】--",
            value="🇩:オリジナルエンティティ・配布MAP・ほぼすべてのコマンドを理解してる人はこちら!\n(execute(複雑),function,etc.)",
            inline=False,
        )

        jebe_embed = discord.Embed(
            title="JE/BE・機種設定", description="ーーーーーーーーーー", color=0x3AFF11
        )
        jebe_embed.add_field(
            name="--【@JE(Java)勢】--",
            value="<:JE:892256704123772931>:Java Editionをプレイしてる人はこちら!",
            inline=False,
        )
        jebe_embed.add_field(
            name="--【@BE(統合)勢】--",
            value="<:BE:892256680509861929>:Bedrock Editionをプレイしてる人はこちら!",
            inline=False,
        )
        jebe_embed.add_field(
            name="--【@PC】--", value="🖥️:パソコンを使ってプレイしてる人はこちら !", inline=False
        )
        jebe_embed.add_field(
            name="--【@スマホ】--", value="📱:スマートフォンを使ってプレイしてる人はこちら!", inline=False
        )
        jebe_embed.add_field(
            name="--【@家庭用ゲーム機】--",
            value="🎮:家庭用ゲーム機(Switch,PS4,PS5,etc.)を使ってプレイしてる人はこちら!",
            inline=False,
        )

        sen_embed = discord.Embed(
            title="宣伝・質問受付設定", description="ーーーーーーーーーー", color=0x3AFF11
        )
        sen_embed.add_field(
            name="--【@宣伝し隊】--", value="📝:宣伝したい人はこのロールを付けて宣伝してください!", inline=False
        )
        sen_embed.add_field(
            name="--【@宣伝ウェルカム】--", value="📩:宣伝はしないけど宣伝チャンネルを見たい人はこちら!", inline=False
        )
        sen_embed.add_field(
            name="--【@DM質問OK】--", value="📮:DMでの質問対応をしてもいいよという方はこちら!", inline=False
        )
        sen_embed.add_field(
            name="--【@java 質問受け付け-メンション可】--",
            value="<:JE:892256704123772931>:Java Edition に関する質問に回答できる方はこちら!",
            inline=False,
        )
        sen_embed.add_field(
            name="--【@be 質問受け付け-メンション可】--",
            value="<:BE:892256680509861929>:Bedrock Edition に関する質問に回答できる方はこちら!",
            inline=False,
        )

        hoka_embed = discord.Embed(
            title="その他設定", description="ーーーーーーーーーー", color=0x3AFF11
        )
        hoka_embed.add_field(
            name="--【@通知ON】--", value="🔔:ゲームの勧誘などの通知が行っても大丈夫な方はこちら!", inline=False
        )
        hoka_embed.add_field(
            name="--【@MEE6レベル無効化】--",
            value="🔏:MEEE6による、レベリング機能がいらないと思った方はこちら!",
            inline=False,
        )
        hoka_embed.add_field(
            name="--【@FOREVER_18】--",
            value="🔞:18禁チャンネル(という名の飯テロチャンネル)を見たい方はこちら !",
            inline=False,
        )
        hoka_embed.add_field(
            name="--【@bump非表示】--",
            value="⤴️:DisboardによるBUMP通知が邪魔だと思った方はこちら!\n(このロールがつくと、<#965098244193542154>が見れなくなります)",
            inline=False,
        )

        await interaction.response.send_message("実行されました", ephemeral=True)
        await interaction.channel.send(embed=role_embed)
        await interaction.channel.send(embed=com_embed)
        await interaction.channel.send(view=CRoleRankButtons())
        await interaction.channel.send(embed=jebe_embed)
        await interaction.channel.send(view=CRoleJEBEButtons())
        await interaction.channel.send(embed=sen_embed)
        await interaction.channel.send(view=CRoleAdButtons())
        await interaction.channel.send(embed=hoka_embed)
        await interaction.channel.send(view=CRoleOtherButtons())


async def setup(bot: commands.Bot):
    await bot.add_cog(CRole(bot))
    bot.add_view(CRoleRankButtons())
    bot.add_view(CRoleJEBEButtons())
    bot.add_view(CRoleAdButtons())
    bot.add_view(CRoleOtherButtons())
