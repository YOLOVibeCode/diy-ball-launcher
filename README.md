# DIY Two-Wheel Soccer Ball Launcher (with Auto Feeder)

A low-cost, two-wheel soccer ball launcher built from used treadmill motors, pneumatic wheels, and plywood, with a gravity ramp + timed paddle gate that feeds balls automatically. Designed for goalkeeper training.

> **Status:** Design spec / build guide. Prices are rough estimates (USD) and vary by source.

---

## Table of Contents
1. [Safety First](#safety-first)
2. [Specifications](#specifications)
3. [How It Works](#how-it-works)
4. [Bill of Materials](#bill-of-materials)
5. [Layout & Dimensions](#layout--dimensions)
6. [Build Steps — Launcher](#build-steps--launcher)
7. [Build Steps — Auto Feeder](#build-steps--auto-feeder)
8. [Wiring](#wiring)
9. [Tuning & Operation](#tuning--operation)
10. [Future Upgrades](#future-upgrades)

---

## Safety First

- **Guard both wheels.** Only the ball gap should be open.
- **Kill switch within reach** of the operator at all times.
- **Start slow.** A two-wheel launcher can throw harder than a human kick.
- **Load from behind only.** Never reach near the wheels while they spin.
- **High-voltage DC.** Treadmill motors run ~90–130 V DC. Enclose all wiring, ground the frame, and follow the controller's wiring diagram exactly.
- **No pneumatic/air-cannon designs.** Pressurized PVC can shatter.
- Keeper should wear full gear (gloves, shin guards). Set feed interval generously at first.

---

## Specifications

| Item | Spec |
|---|---|
| Ball | Size 5 soccer ball (~8.6–8.8 in / 22 cm diameter) |
| Launch method | Two counter-rotating pneumatic wheels |
| Wheels | 2 × 10 in pneumatic (hand-truck / wheelbarrow) |
| Wheel gap | 7.5–8 in (adjustable via slotted motor mount) |
| Motors | 2 × used treadmill DC motors, ~90–130 V, 1.5–3 HP |
| Motor control | 2 × 120 V AC-input DC motor speed controllers (≈2 HP) — independent speed per wheel |
| Spin / curve | Achieved by running wheels at different speeds |
| Elevation | Hinged base + threaded rod, ~0–30° |
| Base | 3/4 in plywood, ~24 × 36 in, on 2×4 frame |
| Feeder | Gravity ramp (PVC rails), 6–8 ball capacity |
| Feed gate | Two-arm paddle on 12 V windshield-wiper motor |
| Feed interval | Adjustable (start at 4–6 s per ball) |
| Power | 120 V AC (launcher) + 12 V DC supply (feeder) |
| Estimated cost | ~$300–500 total new; ~$200–300 with scavenged motors |

---

## How It Works

```
   SIDE VIEW (simplified)

                                  ball ramp (PVC rails, 5–10° slope)
                       o  o  o  o  o
   SHOT  <---  [WHEELS]<--[GATE]<--------------------------
     <==       (o)  (o)    paddle
              ===========================
              base (tilts on rear hinge)
```

1. Balls sit single-file on a sloped PVC ramp behind the launcher.
2. A rotating paddle gate releases **one ball per half-turn** into the feed chute.
3. The ball rolls into the gap between two counter-rotating wheels.
4. The wheels squeeze and fling the ball forward. Wheel speed = shot power; speed difference = curve.

---

## Bill of Materials

### Launcher

| Part | Qty | Est. Cost | Notes |
|---|---|---|---|
| Treadmill DC motor (90–130 V, 1.5–3 HP) | 2 | $0–40 ea | Facebook Marketplace, curbside, repair shops |
| DC motor speed controller, 120 V AC in, ~2 HP | 2 | $30–50 ea | One per motor |
| 10 in pneumatic wheel | 2 | $12–20 ea | Hand-truck or wheelbarrow style |
| Shaft-to-wheel hub adapter | 2 | $10–25 ea | Match motor shaft (often 1/2 in or 5/8 in); or bolt to treadmill flywheel |
| 3/4 in plywood, 4 × 4 ft | 1 | $35–50 | Base + guards |
| 2×4 × 8 ft | 3 | $15 | Under-frame / motor clearance |
| Door hinge (3 in, heavy) | 2 | $8 | Tilt hinge |
| 1/2 in threaded rod + wing nut + washers | 1 set | $8 | Elevation adjust |
| 5/16 in carriage bolts, nuts, washers; wood screws | assorted | $15 | |
| Expanded metal sheet (or plywood) | 1 | $15–20 | Wheel guards |
| Heavy-duty switched power strip / paddle kill switch | 1 | $15–25 | Master cutoff |
| 12 AWG outdoor extension cord | 1 | $25–35 | |
| Project box / enclosure for controllers | 1 | $10–20 | |

### Auto Feeder

| Part | Qty | Est. Cost | Notes |
|---|---|---|---|
| 1 in PVC pipe, 10 ft | 3 | $15–25 | Rails, hoops, legs |
| 1 in PVC elbows / tees | ~12 | $10 | |
| 12 V windshield-wiper motor | 1 | $20–35 | Slow, high torque; junkyard or online |
| 12 V PWM motor speed controller | 1 | $10–15 | Sets feed rate |
| 12 V power supply, 10 A (or car battery) | 1 | $20–30 | |
| Toggle switch | 1 | $5 | Pause feeder independently |
| Plywood scrap | — | $0 | Two-arm paddle |

---

## Layout & Dimensions

```
   TOP VIEW  (front = top of diagram)

               ^  SHOT EXITS
               |
     +-----------------------------+
     |   ( W )   ( BALL )   ( W )  |   W = 10 in wheel, motor under board
     |    -->               <--    |   wheels spin TOWARD each other
     |      |<- 7.5–8 in ->|       |
     |          [ CHUTE ]          |
     |          [   ^   ]          |   feed chute from rear
     |          [   |   ]          |
     +=============================+   <-- tilt hinge (rear edge)
          base ~24 in W x 36 in D
```

- **Wheel centers:** ~18 in apart (10 in wheels + 7.5–8 in gap). Fine-tune with slotted holes.
- **Wheel height:** wheel centers ≈ ball center height (~4.3 in above chute floor).
- **Chute:** ~10 in wide, lined with plywood or a split 4 in PVC, centered on the wheel gap.
- **Motor clearance:** 2×4 frame under the board gives room for motor bodies.

---

## Build Steps — Launcher

1. **Cut the base** — 3/4 in plywood, ~24 × 36 in.
2. **Build the under-frame** — 2×4 perimeter plus a front cross-brace for stiffness.
3. **Mark wheel centers** — ~18 in apart, ~6 in from the front edge, centered left-to-right.
4. **Drill shaft holes** — motors mount underneath; shafts come up through the board.
5. **Mount motors** — one fixed; one on **slotted holes** to adjust the gap.
6. **Attach wheels** — via hub adapters or bolted to the treadmill flywheels. Wheels should sit just above the board surface.
7. **Set gap** — 7.5–8 in between tire surfaces. Test with a ball: it should need firm pressure to pass through.
8. **Install chute** — centered on the gap, running to the rear edge.
9. **Add guards** — enclose both wheels; leave only the ball path open.
10. **Tilt mechanism** — hinge the rear edge to a second base board; threaded rod + wing nut at the front sets the angle.

---

## Build Steps — Auto Feeder

1. **Ramp rails** — two PVC rails ~6–7 in apart, 5–6 ft long.
2. **Containment** — a third top rail or PVC hoops every ~18 in to keep balls from rolling off.
3. **Legs / slope** — PVC legs so the ramp drops 5–10° toward the launcher and ends level with the chute entrance.
4. **Paddle gate** — cut a two-arm (turnstile-style) plywood paddle; arms long enough to block one ball.
5. **Mount wiper motor** — beside the ramp end, paddle on the crank. Only **one ball** should fit between the paddle and the chute.
6. **Test by hand** — rotate the paddle manually; confirm exactly one ball releases per half-turn.

---

## Wiring

### Launcher (120 V AC → DC motors)
```
Wall outlet -> Kill switch / switched strip -> Controller A -> Motor A
                                            -> Controller B -> Motor B
```
- Controllers and terminals inside a closed enclosure.
- Ground the frame / metal guards.
- Follow each controller's diagram for armature (+/−) wiring. Swap motor leads to reverse direction so the wheels spin **toward each other**.

### Feeder (12 V DC)
```
12 V supply -> Toggle switch -> PWM controller -> Wiper motor
```
- Use the wiper motor's low-speed lead.
- Keep feeder power separate from launcher power so you can pause feeding while wheels spin.

---

## Tuning & Operation

| Goal | Adjustment |
|---|---|
| Softer shots | Lower both wheel speeds |
| Harder shots | Raise both wheel speeds (increase gradually) |
| Curve left/right | Run one wheel faster than the other |
| Ground balls | Base flat (0°) |
| High balls / crosses | Raise front with threaded rod |
| Ball jams in gap | Widen gap slightly or check tire pressure |
| Weak / inconsistent shots | Narrow gap slightly; match tire pressure on both wheels |
| Feed too fast/slow | Adjust PWM controller on feeder |

**Startup checklist**
1. Area clear; keeper in position and ready.
2. Guards on, wiring enclosed.
3. Wheels on at **low** speed.
4. Feeder on; confirm interval.
5. Increase speed gradually.

**Shutdown:** Feeder off → wheels off → master kill switch → unplug.

---

## Future Upgrades

- **Microcontroller control** (ESP32 / Arduino) for preset drills: random speed, angle, and spin.
- **Phone remote** over Wi-Fi/Bluetooth for start/stop and feed rate.
- **Pan base** (lazy-susan bearing + servo) to randomize left/right shot direction.
- **Shot counter / session log** for training stats.
- **Tachometer** (hall sensor) on each wheel for repeatable speeds.

---

## License

MIT — build, modify, and share freely. Use at your own risk.
