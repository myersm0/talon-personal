app: /term*/i

-

cargo build:
	insert("cargo build")
	key(enter)

cargo build release:
	insert("cargo build --release")
	key(enter)

cargo test:
	insert("cargo test")
	key(enter)

cargo run:
	insert("cargo run")
	key(enter)

cargo run binary:
	insert("cargo run --bin ")

