import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer

class SentdeBot(sc.BotAI):
    async def on_step(self, iteration):
        await self.distribute_workers()
        await self.build_workers()
       

        from sc2.constants import HATCHERY, DRONE
        async def build_workers(self):
            for hatchery in self.units(HATCHERY).ready.noqueue:
                if self.can_afford(DRONE):
                    await self.do(hatchery.train(DRONE))

    class SentdeBot(sc2.BotAI)
    async def on_step(self, iteration):
        await self.distribute_workers()
        await self.build_workers()
        await self.build_overlords()
        await self.expand()

        async def build_workers(self):
            if self.supply_left < 5 and not self.already_pending(OVERLORD):
                larva = self.units(LARVA).random
                if self.can_afford(DRONE):
                    await self.do(larva.train(DRONE))


from sc2.constants import OVERLORD, LARVA, DRONE, EXTRACTOR, HATCHERY
class SentdeBot(sc2.BotAI)
async def on_step(self, iteration):
    await self.distribute_workers()
    await self.build_workers()
    await self.build_overlords()
    await self.expand()
    await self.build_extractor()

    async def build_assimilator(self):
        for hatchery in self.units(HATCHERY).ready:
            vespenes = self.state.vespene_geyser.closer_than(20.0, hatchery)
            for vespene in vespenes:
                if notself.can_afford(EXTRACTOR):
                    break

    async def build_extractor(self):
        for hatchery in self.units(HATCHERY).ready:
            vespenes = self.state.vespene_geyser.closer_than(20.0, hatchery)
            for vespene in vespenes:
                if not self.can_afford(EXTRACTOR):
                    break
                worker = self.select_build_worker(vespene.position)
                if worker is None:
                    break

                if not self.units(EXTRACTOR).closer_than(1.0, vespene).exists:
                    await self.do(worker.build(EXTRACTOR, vespene))
class SentdeBot(sc2.BotAI)
async def on_step(self, iteration):
    await self.distribute_workers()
    await self.build_workers()
    await self.build_overlords()
    await self.expand()
    await self.build_extractor()
    await self.build.offensive_buildings()

    async def build_offensive_buildings(self):
        if.self.units(SPAWNINGPOOL).ready.exists:
            if self.can_afford(ROACHWARREN) and not self.units(ROACHWARREN):
                await self.build(ROACHWARREN, near=self.units(SPAWNINGPOOL).first)

class SentdeBot(sc2.BotAI)
async def on_step(self, iteration):
    await self.distribute_workers()
    await self.build_workers()
    await self.build_overlords()
    await self.expand()
    await self.build_extractor()
    await self.build.offensive_buildings()
    await self.build_offensive_units()
    await self.build_offensive_force()

async def build_offensive_force(self):
    for gw in self.units(HATCHERY).ready:
        if self.can_afford(ZERGLING) and self.supply_left > 0:
            await self.do(gw.train(ZERGLING))

class SentdeBot(sc2.BotAI)
async def on_step(self, iteration):
    await self.distribute_workers()
    await self.build_workers()
    await self.build_overlords()
    await self.expand()
    await self.build_extractor()
    await self.build.offensive_buildings()
    await self.build_offensive_units()
    await self.build_offensive_force()
    await self.attack()

    async def attack(self):
        if self.units(ZERGLING).amount > 10:
            for s in self.units(ZERGLING).idle:
                await self.do(s.attack(self.find_target(self.state)))

async def attack(self):
    if self.units(ZERGLING).amount > 10:
        for s in self.units(ZERGLING).idle:
            await self.do(s.attack(self.find_target(self.state)))
            elif self.units(ZERGLING).amount > 20:
                if len(self.known_enemy_units) > 0:
                    for s in self.units(ZERGLING).idle:
                        await self.do(s.attack(random.choice(self.known_enemy_units)))

def find_target(self, state):
    if len(self.known_enemy_units) > 0:
        return random.choice(self.known_enemy_units)
    elif len(self.known_enemy_structures) > 0:
        return random.choice(self.known_enemy_structures)
    else:
        return self.enemy_start_locations[0]

run_game(maps.get("AbyssalReefLE"), [
            Bot(Race.Zerg, SentdeBot()),
            Computer(Race.Terran, Difficulty.hardest)
        ], realtime=True)