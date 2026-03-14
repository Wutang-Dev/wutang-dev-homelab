# Project 14 – Sunshine + Moonlight LAN Game Streaming

## Overview

This project documents the deployment of a LAN-based game streaming environment using Sunshine and Moonlight within my WuTang homelab infrastructure.

The goal was to enable high-performance game streaming from my primary gaming server to a secondary PC located in another room while maintaining low latency and high visual quality.

This effectively creates a personal cloud gaming environment within the local network.

---

## Infrastructure

Host System (Jellyfin Server)

GPU: NVIDIA RTX 4070  
Streaming Host: Sunshine  
Encoder: NVENC hardware encoding

Client System (Bedroom PC)

GPU: AMD RX 5500XT  
Streaming Client: Moonlight

Network

Local LAN via WuTangLAN router

---

## Architecture

Gaming Server (RTX 4070)
↓
Sunshine (NVENC hardware encoding)
↓
Local Area Network
↓
Moonlight Client
↓
Bedroom Gaming PC

---

## Configuration

Sunshine Configuration

Encoder: NVIDIA NVENC  
Preset: P7 (highest quality preset)  
Codec: HEVC 10-bit  
Two-pass encoding enabled

Moonlight Configuration

Resolution: 1080p  
Frame Rate: 120 FPS  
Bitrate: 150 Mbps  

---

## Performance Results

Observed metrics using Moonlight performance overlay:

Average network latency: ~1 ms  
Frame drops: 0%  
Decoding latency: ~0.25 ms  
Stable frame rate: ~120 FPS  

Gameplay was tested across multiple titles including:

- FIFA 16 Classic Mod
- Fight Night Champion Mod
- Spider-Man Remastered

The streaming experience was smooth with minimal visual degradation compared to playing directly on the host machine.

---

## Lessons Learned

Hardware encoding significantly improves streaming performance and reduces CPU load.

Network stability is more important than raw bandwidth for consistent frame delivery.

HEVC provides improved image quality at the same bitrate compared to H264.

Proper encoder configuration (NVENC preset and bitrate tuning) can noticeably improve stream clarity.

---

## Future Improvements

Possible future improvements include:

Testing 1440p streaming  
Implementing remote streaming using Tailscale  
Integrating Playnite for unified game launching  
Evaluating wired network connection for the client system
