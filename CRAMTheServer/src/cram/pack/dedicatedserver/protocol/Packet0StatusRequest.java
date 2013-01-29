package cram.pack.dedicatedserver.protocol;

import cram.pack.dedicatedserver.NetServerHandler;

public class Packet0StatusRequest extends Packet{
	public Packet0StatusRequest() {
		PacketID=0;
	}
	@Override
	public void handle(NetServerHandler handler) {
		handler.handlePacket0StatusRequest(this);
	}
}
