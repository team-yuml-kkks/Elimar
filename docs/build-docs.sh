#!/bin/sh

set -e

REPO="$1" ### Path to the repository.
WIKI_PAGE="$2" ### Name of the WIKI file.
DOCS_PATH="$3" ### Path to the C4 files.
APP_NAME="$4"

### Generate hashes of the files to remove caching issues.
### Using -hex to not generate the `/` inside a hash.
CONTEXT_FILE="$(openssl rand -hex 12)_context.svg"
SYSTEM_FILE="$(openssl rand -hex 12)_system.svg"

### Recreate diagrams directory.
rm -rf "$REPO.wiki/diagrams/"
mkdir "$REPO.wiki/diagrams/"

### Copy diagrams with hash.
cp "$DOCS_PATH/context.svg" "$REPO.wiki/diagrams/$CONTEXT_FILE"
cp "$DOCS_PATH/$APP_NAME/system.svg" "$REPO.wiki/diagrams/$SYSTEM_FILE"

cd $REPO.wiki

### Set git configs to push to the WIKI
git config --global user.email "kamil.supera.ks@gmail.com"
git config --global user.name "Kamil Supera"

### Create wiki page based on the template with injected hashed files.
cat > "$WIKI_PAGE" <<- EOM
## C1 Diagram
![context_diagram](./diagrams/$CONTEXT_FILE)
## C2 Diagram
![system_diagram](./diagrams/$SYSTEM_FILE)
EOM

### Push changes to the WIKI.
git add diagrams/
git add "$WIKI_PAGE"

git diff-index --quiet HEAD || git commit -m "Update diagrams"
git push
